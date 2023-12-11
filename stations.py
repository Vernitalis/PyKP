#!/usr/bin/env python3

import requests
import json
import folium
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy import String, Float, Integer
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.orm import Mapped, mapped_column


class OverpassQuery:
    endpoint = "https://overpass-api.de/api/interpreter"

    def __init__(self, query: str):
        self.query = query
        self._cache_filepath = ""

    @classmethod
    def from_file(cls, filepath: str):
        with open(filepath, "r") as file:
            query = file.read()
        new_object = cls(query)
        new_object._cache_filepath = ".{name}_cache.json".format(name=filepath.split(".")[0])
        return new_object

    def run(self):
        cache_file = Path(self._cache_filepath)
        if cache_file.is_file():
            return json.loads(cache_file.read_text())
        response = requests.post(self.endpoint, data=self.query)
        if not cache_file.exists():
            cache_file.write_text(response.text)
        return json.loads(response.text)


class Base(DeclarativeBase):
    pass


class Station(Base):
    __tablename__ = "stations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    lattitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)

    def __init__(self, name: str, lattitude: float, longitude: float):
        self.name = name
        self.lattitude = lattitude
        self.longitude = longitude


if __name__ == "__main__":
    mymap = folium.Map(location=[52.0, 19.0],
                       zoom_start=7,
                       tiles='https://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png',
                       attr='Map data: {attribution.OpenStreetMap} | Map style: &copy;'
                            ' <a href="https://www.OpenRailwayMap.org">OpenRailwayMap</a> '
                            '(<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
                       )
    folium.GeoJson("poland_outline.geojson",
                   style_function=lambda feature: {"color": "black",
                                                   "fillColor": "#fff000",
                                                   "stroke-width": 1,
                                                   "fill-opacity": 0.3},
                   ).add_to(mymap)
    engine = create_engine("sqlite:///baza.db", echo=True)
    Base.metadata.create_all(engine)
    stations_query = OverpassQuery.from_file("stations.ql")
    stations_query_result = stations_query.run()
    with Session(engine) as session:
        stations = []
        for e in stations_query_result["elements"]:
            try:
                stations.append(Station(e["tags"]["name"], e["lat"], e["lon"]))

            except(Exception):
                pass

        # session.add_all(stations)
        # session.commit()

        for station in stations:
            custom_icon = folium.CustomIcon(icon_image='point.png',icon_size=(7, 7),)
            folium.Marker(
                location=[station.lattitude, station.longitude],
                icon=custom_icon,
                popup=station.name,
            ).add_to(mymap)

        mymap.save("mapa.html")
