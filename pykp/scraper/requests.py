import scrapy
from urllib.parse import urlencode


class UrlEncodedRequest(scrapy.Request):
    def __init__(self, url, headers={}, data={}, **kwargs):
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        super().__init__(
            url=url, method="POST", headers=headers, body=urlencode(data), **kwargs
        )
