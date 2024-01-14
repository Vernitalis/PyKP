from pathlib import Path
from scrapy.exceptions import NotConfigured
from scrapy.utils.conf import closest_scrapy_cfg
import datetime


class SetupLogFile:
    def __init__(self, crawler, log_file) -> None:
        super().__init__()
        self.crawler = crawler
        self.log_file = log_file

    @classmethod
    def from_crawler(cls, crawler):
        logs_prefix = crawler.settings.get("LOGS_PREFIX")
        if crawler.settings.get("LOG_FILE") or not logs_prefix:
            raise NotConfigured

        logs_dir_name = crawler.settings.get("LOGS_DIR") or "logs"
        project_root = Path(closest_scrapy_cfg(__file__)).parent
        logs_dir = project_root / logs_dir_name
        logs_dir.mkdir(exist_ok=True, parents=True)

        date_str = datetime.datetime.now().isoformat()
        log_file_name = "{prefix}_{date_str}.txt".format(
            prefix=logs_prefix, date_str=date_str
        )

        log_file = str(logs_dir / log_file_name)
        return cls(crawler, log_file)

    def update_settings(self, settings):
        settings.set("LOG_FILE", self.log_file, "addon")
