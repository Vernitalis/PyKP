from pathlib import Path
from scrapy.exceptions import NotConfigured
from scrapy.utils.conf import closest_scrapy_cfg
import datetime


class SetupLogFile:
    def update_settings(self, settings):
        if settings.get("LOG_FILE"):
            raise NotConfigured("LOG_FILE is set. Skipping log file setup...")

        logs_prefix = settings.get("BOT_NAME").lower().replace(" ", "_")
        logs_dir_name = "logs"

        project_root = Path(closest_scrapy_cfg(__file__)).parent
        logs_dir = project_root / logs_dir_name
        logs_dir.mkdir(exist_ok=True, parents=True)

        date_str = datetime.datetime.now().isoformat()
        log_file_name = "{prefix}_{date_str}.txt".format(
            prefix=logs_prefix, date_str=date_str
        )

        log_file = str(logs_dir / log_file_name)
        settings.set("LOG_FILE", log_file, "addon")
