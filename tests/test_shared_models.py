from django.test import TestCase
from pykp.shared.models import Station


class StationModelTest(TestCase):

    def test_station_creation(self):
        station_data = {
            "id": 1,
            "name": "Test Station",
            "nz": "NZ123",
            "iso": "ISO123",
            "key": "station_key",
        }
        station = Station.from_dict(station_data)

        self.assertTrue(isinstance(station, Station))
        self.assertEqual(station.id, station_data["id"])
        self.assertEqual(station.name, station_data["name"])
        self.assertEqual(station.nz, station_data["nz"])
        self.assertEqual(station.iso, station_data["iso"])
        self.assertEqual(station.key, station_data["key"])

    def test_station_meta_db_table(self):
        self.assertEqual(Station._meta.db_table, "stations")