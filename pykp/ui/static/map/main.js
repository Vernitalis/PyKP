const countryOutlineStyle = new ol.style.Style({
	fill: undefined,
	stroke: new ol.style.Stroke({
		color: [0, 0, 255],
		width: 3
	})
})

const osmLayer = new ol.layer.Tile({
	source: new ol.source.OSM()
});

const railwayLayer = new ol.layer.Tile({
	source: new ol.source.OSM({
		url: "http://tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png",
		crossOrigin: null,
		opaque: false
	})
});

const countryOutlineLayer = new ol.layer.Vector({
	source: new ol.source.Vector({
		format: new ol.format.GeoJSON(),
		url: "https://polygons.openstreetmap.fr/get_geojson.py?id=49715&params=0.010000-0.010000-0.010000"
	}),
	style: countryOutlineStyle
})

const homeMap = new ol.Map({
	target: 'map-container',
	layers: [osmLayer, railwayLayer, countryOutlineLayer],
	view: new ol.View({
		center: ol.proj.fromLonLat([19, 52]),
		zoom: 6,
		constrainResolution: true
	})
});
