import json
import collections
from pprint import pprint
import xml.etree.ElementTree as ET


def read_json(file_path, len_word=6, top_words=10):
   with open(file_path, 'r', encoding='utf-8') as news_file:
       news = json.load(news_file)
       description_words = []
       for item in news['rss']['channel']['items']:
           description = [word for word in item['description'].split(' ') if len(word) > len_word]
           description_words.extend(description)
       counter_words = collections.Counter(description_words)
       pprint(counter_words.most_common(top_words))