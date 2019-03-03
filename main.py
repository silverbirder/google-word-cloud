from takeout import Takeout
from google_word_cloud import GoogleWordCloud

ROOT_PATH = 'Takeout/'

takeout = Takeout(path=ROOT_PATH)
takeout.init()
takeout.parse_original()
takeout.init()
takeout.parse_extract(files=takeout.split_json_files)
takeout.init()
google_word_cloud = GoogleWordCloud(takeout.split_txt_files)
google_word_cloud.out_put()
