from ..items import CredentialsItem
import re
import scrapy


class CredentialsSpider(scrapy.Spider):
    name = "credentials"
    allowed_domains = ["portalpasazera.pl"]
    start_urls = ["https://www.portalpasazera.pl"]

    @classmethod
    def update_settings(cls, settings):
        super().update_settings(settings)
        settings.setdefault("ITEM_PIPELINES", {}).update(
            {"pykp.scraper.pipelines.EnvironmentVariableOutput": 1000}
        )

    def parse(self, response):
        cookies = [c.decode() for c in response.headers.getlist("Set-Cookie")]
        cookies_filter = filter(
            lambda c: c.startswith("__RequestVerificationToken"), cookies
        )

        token_cookie = next(cookies_filter)

        headers = {}
        cookies = {
            "__RequestVerificationToken": token_cookie.split("; ")[0].split("=")[1]
        }

        for script in response.xpath("/html/body/script/text()").getall():
            try:
                key_value = re.fullmatch(
                    r"\$\.ajaxSetup\({ headers: { '(.*)' } }\);", script
                )[1].split("': '")
                headers[key_value[0]] = key_value[1]
            except Exception:
                pass

        token = response.xpath(
            '//input[@name="__RequestVerificationToken"]/@value'
        ).get()
        headers["__RequestVerificationToken"] = token

        yield CredentialsItem(token=token, headers=headers, cookies=cookies)
