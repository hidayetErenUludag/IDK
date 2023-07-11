import json
import time

import requests

url = "http://192.168.1.19:8080/jsonrpc"

cookies_string = None


def auther():
    global cookies_string
    if cookies_string is None:
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "login",
            "params": {"user": "admin", "passwd": "admin"}
        }
        auth = requests.post(url, json=payload, verify=False)
        cookies_string = auth.cookies
    return cookies_string


def get_th_id():
    payload = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "new_trans",
        "params": {"db": "running", "mode": "read"}
    }
    req = requests.post(url, cookies=auther(), json=payload, verify=False)
    response = req.text
    th_id = json.loads(response)["result"]["th"]

    return th_id


def transaction_info():
    get_th_id()
    time.sleep(1)
    payload = {
        "jsonrpc": "2.0",
        "id": 11,
        "method": "get_trans"
    }
    response = requests.post(url, cookies=auther(), json=payload, verify=False)
    st_response = response.text
    x = json.loads(st_response)["result"]["trans"][0]["db"]
    return x


print(transaction_info())
