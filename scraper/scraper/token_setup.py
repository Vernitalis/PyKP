# from scraper.spiders import CredentialsSpider
import requests # try to omit requests
import re
from scrapy.http import HtmlResponse 
from scraper.items import CredentialsItem

class TokenSetupAddon:
    @staticmethod
    def requests_to_scrapy(rr: requests.Response):
        return HtmlResponse(url=rr.url,status=rr.status_code,headers=rr.headers,body=rr.content)
    
    @classmethod
    def get_credentials(cls, headers):
        start_url = "https://www.portalpasazera.pl"
        requests_response = requests.get(start_url)
        response = cls.requests_to_scrapy(requests_response)

        cookies = response.headers["Set-Cookie"].decode().split(", ")
        cookies_filter = filter(
            lambda c: c.startswith("__RequestVerificationToken"), cookies
        )
        token_cookie_str = next(cookies_filter)
        token_cookie = token_cookie_str.split("; ")[0]

        scripts = response.xpath("/html/body/script/text()").getall()

        headers = {}
        for s in scripts:
            try:
                key_value = re.fullmatch(r"\$\.ajaxSetup\({ headers: { '(.*)' } }\);", s)[1].split("': '")
                headers[key_value[0]] = key_value[1]
            except(Exception):
                pass

        body_token = response.xpath('//input[@name="__RequestVerificationToken"]/@value').get()
        header_token = token_cookie.split("=")[1]
        
        return CredentialsItem(body_token=body_token, header_token=header_token, headers=headers)

    def update_settings(self, settings):
        request_headers = {
            "User-Agent": settings.get("USER_AGENT")
        }
        credentials = self.get_credentials(request_headers)
        default_headers: dict = settings.getdict("DEFAULT_REQUEST_HEADERS")
        default_headers.update(credentials["headers"])
        settings.set("DEFAULT_REQUEST_HEADERS", default_headers)
        settings.set("PP_BODY_TOKEN", credentials["body_token"])
        settings.set("PP_COOKIE_TOKEN", credentials["header_token"])
