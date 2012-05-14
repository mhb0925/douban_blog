from pymongo import Connection
import douban.service

connection = Connection()
db = connection['douban_blog']

API_KEY = '0559f4af5d728327100dde0e18578975'
DOUBAN_UID = '28878608'
MAX_RESULTS = 5

douban_client = douban.service.DoubanService(api_key = API_KEY)
