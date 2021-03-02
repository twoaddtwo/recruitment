import requests
import unittest
import json
from Common import common


class Login(unittest.TestCase):

    def login(self, url, headers, data):
        r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)

        print(r.json()['data']['token'])
        return r.json()['data']['token']


