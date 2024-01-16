from django.contrib.gis.db import models


class Location(models.Model):
    id = models.IntegerField(
        primary_key=True
    )  # TODO: autoincrement or switch to name as primary key
    name = models.TextField()
    point = models.PointField()
    type = models.TextField()  # TODO: add validator

    class Meta:
        db_table = "locations"
