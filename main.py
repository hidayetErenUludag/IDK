import requests

login = "http://192.168.1.14:8080/jsonrpc"
username = "admin"
password = "admin"

session = requests.session()


def loger(user, passw):
    response = session.post(login,
                            json={"jsonrpc": "2.0", "method": "login", "params": {"user": user, "passwd": passw},
                                  "id": 2})

    if response.status_code == 200 and "result" in response.json():
        print("Login Successful! ")
        print(session.cookies.values())
        return True
    else:
        print("Login failed.")
        return False


def get_trans():
    print(loger(username, password))
    response = session.get("http://192.168.1.14:8080/webui-one/ServiceManager/l3vpn:vpn/l3vpn",
                           json={"jsonrpc": "2.0", "method": "get_trans", "params": {}, "id": 289})
    print(response.url)


get_trans()
