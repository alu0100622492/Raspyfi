#import json
import firebase_admin
from firebase_admin import credentials

# from pprint import pprint

# with open("data.json", "r") as read_file:
#     data = json.load(read_file)

# with open('data.json') as f:
#     data = json.load(f)

# pprint(data)

# data1 = json.loads('data.json').read()
# data = json.loads(open('data.json').read())
# json.dumps(data)
# print('eo', data)
# print('eoi',data)

cred = credentials.Certificate(json.loads('data.json'))
default_app = firebase_admin.initialize_app(cred)
