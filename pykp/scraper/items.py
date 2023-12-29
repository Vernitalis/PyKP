from scrapy import Field, Item

class CredentialsItem(Item):
    cookies = Field()
    headers = Field()
    token = Field()

class StationItem(Item):
    id = Field()
    iso = Field()
    key = Field()
    name = Field()
    nz = Field()

class TrainItem(Item):
    carrier = Field()
    departure = Field()
    destination = Field()
    id = Field()
    name = Field()
    platform = Field()
    start = Field()
    track = Field()
    url = Field()
