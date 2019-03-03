import datetime
import ijson
import json
import os

from dateutil.relativedelta import relativedelta


class Takeout(object):

    def __init__(self, path, all=False):
        self.path = path
        self.original_files = []
        self.split_json_files = []
        self.split_txt_files = []
        self.all = all

    def init(self):
        self.original_files = []
        self.split_json_files = []
        self.split_txt_files = []

        if not self.path:
            return
        if not os.path.exists(self.path):
            return
        for pathname, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                if filename == 'マイアクティビティ.json':
                    self.original_files.append(f'{pathname}/{filename}')
                elif filename.endswith('.json'):
                    self.split_json_files.append(f'{pathname}/{filename}')
                elif filename.endswith('.txt'):
                    self.split_txt_files.append(f'{pathname}/{filename}')

    def parse_original(self):
        for file in self.original_files:
            with open(file) as f:
                items = ijson.items(f, 'item')

                def output(file, data):
                    with open(file, 'w') as j:
                        json.dump(data, j, indent=4, ensure_ascii=False)

                dump_data = []
                base_day = datetime.datetime.today()
                base_day = datetime.date(base_day.year, base_day.month, 1)

                for item in items:
                    try:
                        item_day = datetime.datetime.strptime(
                            item.get('time'), '%Y-%m-%dT%H:%M:%S.%f%z')
                    except ValueError:
                        item_day = datetime.datetime.strptime(
                            item.get('time'), '%Y-%m-%dT%H:%M:%S%z')
                    item_day = datetime.date(item_day.year, item_day.month, 1)
                    if base_day != item_day:
                        output(f'{file}.{base_day.year}{str(base_day.month).zfill(2)}.json', dump_data)
                        dump_data = [item]
                        base_day = base_day - relativedelta(months=1)
                    else:
                        dump_data.append(item)

                if len(dump_data) > 0:
                    output(f'{file}.{base_day.year}{str(base_day.month).zfill(2)}.json', dump_data)

    def parse_extract(self, files):
        for file in self.split_json_files:
            if file in files or self.all:
                with open(file) as f:
                    items = ijson.items(f, 'item')

                    def output(file, list_data):
                        with open(file, 'w') as f:
                            for x in list_data:
                                f.write(str(x) + '\n')

                    search_word_list = []
                    for item in items:
                        title = item.get('title')
                        if title.startswith('検索結果:'):
                            search_word = title[6:].split()
                            search_word_list.extend(search_word)
                    output(file=f'{file}.txt', list_data=search_word_list)
