from django.db import models


class Station(models.Model):
    # name = models.TextField(primary_key=True)
    name = models.TextField()
    nz = models.TextField()
    id = models.IntegerField(primary_key=True)
    key = models.TextField()
    iso = models.TextField()

    class Meta:
        db_table = "stations"

    @classmethod
    def from_dict(cls, dictionary):
        return cls(
            id=dictionary["ID"],
            name=dictionary["Nazwa"],
            nz=dictionary["NZ"],
            iso=dictionary["Iso"],
            key=dictionary["Key"],
        )


class Location(models.Model):
    id = models.IntegerField(
        primary_key=True
    )  # TODO: autoincrement or switch to name as primary key
    name = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    type = models.TextField()  # TODO: add validator

    class Meta:
        db_table = "locations"
