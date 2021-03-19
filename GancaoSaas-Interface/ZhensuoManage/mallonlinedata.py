import requests
import json
from Common import common

headers = common.headers


def save_mallbanner():
    url = "https://test.igancao.cn:8000/gateway/pharmacy/config/saveMallBanner"
    data = {
            "bannerUrls": ["https://storage.test.igancao.cn/mall/202103/PP1615528762879.JPG",
                           "https://storage.test.igancao.cn/mall/202103/DE1615528762887.JPG",
                           "https://storage.test.igancao.cn/mall/202103/AV1615528753286.JPG",
                           "https://storage.test.igancao.cn/mall/202103/MF1615528753302.JPG",
                           "https://storage.test.igancao.cn/mall/202103/1615518490818.jpg"]
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


def create_mallplate():
    url = "https://test.igancao.cn:8000/gateway/pharmacy/config/saveMallPlate"
    data = {
            "id": "",
            "name": "斤斤计较"
            }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    return r.json()


