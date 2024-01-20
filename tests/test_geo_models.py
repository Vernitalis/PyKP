from django.test import TestCase
from django.contrib.gis.geos import Point, Polygon, MultiPolygon, LinearRing
from pykp.geo.models import Location, Outline


class LocationModelTest(TestCase):
    def test_location_creation(self):
        location_data = {
            "id": 1,
            "name": "Test Location",
            "point": Point(x=1.0, y=2.0),
            "type": "Test Type",
        }
        location = Location(**location_data)
        location.save()

        retrieved_location = Location.objects.get(id=1)

        self.assertEqual(retrieved_location.id, location_data["id"])
        self.assertEqual(retrieved_location.name, location_data["name"])
        self.assertEqual(retrieved_location.point, location_data["point"])
        self.assertEqual(retrieved_location.type, location_data["type"])


class OutlineModelTest(TestCase):
    def test_outline_creation(self):
        outline_data = {
            "osm_relation_id": 123,
            "polygon": MultiPolygon(Polygon(LinearRing((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))),
        }
        outline = Outline(**outline_data)
        outline.save()

        retrieved_outline = Outline.objects.get(osm_relation_id=123)

        self.assertEqual(retrieved_outline.osm_relation_id, outline_data["osm_relation_id"])
        self.assertEqual(retrieved_outline.polygon, outline_data["polygon"])