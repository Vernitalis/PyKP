from pathlib import Path
from scrapy.crawler import Crawler
from scrapy.exceptions import NotConfigured
from scrapy.utils.conf import closest_scrapy_cfg
import datetime


class SetupLogFile:
    def __init__(self, spider):
        self.spider = spider

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        return cls(crawler.spider)

    def update_settings(self, settings):
        if settings.get("LOG_FILE"):
            raise NotConfigured("LOG_FILE is set. Skipping log file setup...")

        logs_dir_name = "logs/scrapy"

        project_root = Path(closest_scrapy_cfg(__file__)).parent
        logs_dir = project_root / logs_dir_name
        logs_dir.mkdir(exist_ok=True, parents=True)

        date_str = datetime.datetime.now().isoformat()
        log_file_name = "{name}_{date_str}.txt".format(
            name=self.spider.name, date_str=date_str
        )

        log_file = str(logs_dir / log_file_name)
        settings.set("LOG_FILE", log_file, "addon")
