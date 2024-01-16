from django.db import models


class Station(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    nz = models.TextField()
    iso = models.TextField()
    key = models.TextField()

    class Meta:
        db_table = "stations"

    @classmethod
    def from_dict(cls, dictionary):
        return cls(
            id=dictionary["id"],
            name=dictionary["name"],
            nz=dictionary["nz"],
            iso=dictionary["iso"],
            key=dictionary["key"],
        )
