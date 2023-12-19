#!/usr/bin/env python3
from scrapy import Spider
from scraper.items import CredentialsItem
import re

class CredentialsSpider(Spider):
    start_urls = ["https://www.portalpasazera.pl"]
    name = "credentials"

    def parse(self, response):
        cookies = [header.decode() for header in response.headers.getlist("Set-Cookie")]
        cookies_filter = filter(
            lambda c: c.startswith("__RequestVerificationToken"), cookies
        )
        token_cookie_str = next(cookies_filter)
        token_cookie = token_cookie_str.split("; ")[0]

        scripts = response.xpath("/html/body/script/text()").getall()
        headers = {}
        for s in scripts:
            try:
                key_value = re.fullmatch("\$\.ajaxSetup\({ headers: { '(.*)' } }\);", s)[1].split("': '")
                headers[key_value[0]] = key_value[1]
            except(Exception):
                pass

        body_token = response.xpath('//input[@name="__RequestVerificationToken"]/@value').get()
        header_token = token_cookie.split("=")[1]
        
        yield CredentialsItem(body_token=body_token,header_token=header_token,headers=headers)
