from django.test import TestCase, RequestFactory
from django.contrib.gis.geos import Point, MultiPolygon, Polygon, LinearRing
from datetime import datetime, timezone

from pykp.geo.views import get_locations, get_outline, refresh_outline
from pykp.geo.models import Location, Outline


class TestViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_locations(self):
        location = Location.objects.create(name="Test Location", point=Point(0, 0), type="Test Type")

        request = self.factory.get('/GetLocations/')
        response = get_locations(request)

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Test Location', response.content)
        self.assertIn(b'Test Type', response.content)
        self.assertIn(b'"coordinates": [0.0, 0.0]', response.content)

    def test_get_outline(self):
        outline = Outline.objects.create(osm_relation_id=49715,
                                         polygon=MultiPolygon(Polygon(
                                             LinearRing((0, 0), (0, 1), (1, 1), (1, 0), (0, 0)))),
                                         last_update=datetime.now(timezone.utc))

        request = self.factory.get('/GetOutline/')
        response = get_outline(request)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'49715', response.content)
        self.assertIn(b'"type": "MultiPolygon"', response.content)
        self.assertIn(b'"last_update":', response.content)
