from itemadapter.adapter import ItemAdapter
import json
import os


class EnvironmentVariableOutput:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.items.append(adapter.asdict())
        return item

    def close_spider(self, spider):
        variable_name = "PYKP_{name}_OUTPUT".format(name=spider.name.upper())
        output = json.dumps(self.items)
        os.environ[variable_name] = output
