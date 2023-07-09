import requests

login = "http://192.168.1.14:8080/jsonrpc"
username = "admin"
password = "admin"
service_vpn3 = "http://192.168.1.14:8080/webui-one/ServiceManager/l3vpn:vpn/l3vpn"
service_commit = "http://192.168.1.14:8080/webui-one/CommitManager"
session = requests.session()


def loger(user, passw):
    response = session.post(login,
                            json={"jsonrpc": "2.0", "method": "login", "params": {"user": user, "passwd": passw},
                                  "id": 2})

    if response.status_code == 200 and "result" in response.json():
        print("Login Successful! ")
        print(response.cookies.get("sessionid_8080"))
        return response.cookies.get("sessionid_8080")
    else:
        return "Login failed."


def create_service():
    sessionid = loger(username, password)
    x = {
        "Cookie": "sessionid_8080=" + sessionid,
        "method": "login"
    }

    configuration = {
        "l3vpn": {
            "name": "volvo",
            "as-number": "65101",
            "endpoints": [
                {
                    "name": "main-office",
                    "ce-device": "ce0",
                    "ce-interface": "GigabitEthernet0/11",
                    "ip-network": "10.10.1.0/24",
                    "bandwidth": "12000000"
                },
                {
                    "name": "branch-office1",
                    "ce-device": "ce1",
                    "ce-interface": "GigabitEthernet0/11",
                    "ip-network": "10.7.7.0/24",
                    "bandwidth": "6000000"
                },
                {
                    "name": "branch-office2",
                    "ce-device": "ce4",
                    "ce-interface": "GigabitEthernet0/18",
                    "ip-network": "10.8.8.0/24",
                    "bandwidth": "300000"
                }
            ],
            "qos-policy": "GOLD"
        }
    }
    print(x)

    response = requests.post(service_vpn3, json=configuration, headers=x)

    if response.status_code == 201:
        print("Configuration created successfully!")
    else:
        print(f"Failed to create configuration. Status code: {response.status_code}")
        print("Response content:")
        print(response.reason)


create_service()
