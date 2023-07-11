import json
import requests

# Define the URL for the JSON-RPC endpoint
url = "http://192.168.1.19:8080/jsonrpc"

# Prepare payload for authentication request
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "login",
    "params": {"user": "admin", "passwd": "admin"}
}

# Send authentication request to obtain cookies
authenticate = requests.post(url, json=payload, verify=False)
cookies_string = authenticate.cookies


# Start a new read transaction
payload = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "new_trans",
    "params": {"db": "running", "mode": "read"}
}

# Send the request with the cookies from authentication
req = requests.post(url, cookies=cookies_string, json=payload, verify=False)
response = req.text

th_id = json.loads(response)["result"]["th"]


# Get the transaction information
payload = {"jsonrpc": "2.0", "id": 11, "method": "get_trans"}
req = requests.post(url, cookies=cookies_string, json=payload, verify=False)
print(req.text)

""""
# Get the list of keys for ztp-fttb entries
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "get_list_keys",
    "params": {"th": th_id, "path": "/ztp-fttb:ztp-fttb"}
}

req = requests.post(url, cookies=cookies_string, json=payload, verify=False)
response = req.text
print(1)
print(json.loads(response))
#ztp_entries = json.loads(response)["result"]["keys"]

# Get specific values for a ztp-fttb entry
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "get_values",
    "params": {
        "th": th_id,
        "path": "/ztp-fttb:ztp-fttb{1.1.1.1}",
        "leafs": ["dhcp_ip", "subnet", "device_model"]
    }
}"""

req = requests.post(url, cookies=cookies_string, json=payload, verify=False)
response = req.text
ztp_entry = json.loads(response)
print("a", ztp_entry)
#ztp_entry["result"]["values"][0]["value"]

# Get values for another ztp-fttb entry
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "get_values",
    "params": {
        "th": th_id,
        "path": "/ztp-fttb:ztp-fttb{192.168.1.19}/new-vs-rma",
        "leafs": ["new"]
    }
}

req = requests.post(url, cookies=cookies_string, json=payload, verify=False)
response = req.text
ztp_entry = json.loads(response)
#ztp_entry["result"]["values"][0]["value"]

# Validate the transaction changes
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "validate_commit",
    "params": {"th": th_id}
}

req = requests.post(url, cookies=cookies_string, json=payload, verify=False)
response = req.text

# Commit the transaction changes
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "commit",
    "params": {"th": th_id}
}

req = requests.post(url, cookies=cookies_string, json=payload, verify=False)
response2 = req.text
print(response2)

# Perform a dry-run-native of the commit
payload1 = {
    "jsonrpc": "2.0",
    "id": 168,
    "method": "commit",
    "params": {"th": th_id, "flags": ["dry-run=native"]}
}
commit = requests.post(url, cookies=cookies_string, json=payload1, verify=False)
print(commit.text)

# Get a list of keys for authentication users
payload10 = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "get_list_keys",
    "params": {"th": 1, "path": "/aaa/authentication/users/user"}
}
paylo = requests.post(url, cookies_string, json=payload10, verify=False)
print(paylo.text)


# Set a value for a specific path
payload = {
    "jsonrpc": "2.0",
    "id": 562,
    "method": "set_value",
    "params": {
        "path": "/acidc-core:acidc/tenants{tenant5}/acidc-pa:port/pa{pa6}/pod",
        "value": "1",
        "th": th_id
    }
}

# Get specific values for an authentication user
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "get_values",
    "params": {
        "th": th_id,
        "path": "/aaa/authentication/users/user{test}",
        "leafs": ["uid", "gid", "password", "ssh_keydir", "homedir"]
    }
}

# Run an action
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "run_action",
    "params": {"th": 1, "path": "/devices/sync-from"}
}

# Create a list entry
payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "create",
    "params": {"th": 2, "path": "/aaa/authentication/users/user{test}"}
}

# Show the configuration for a specific path
payload = {
    "jsonrpc": "2.0",
    "id": 45,
    "method": "show_config",
    "params": {
        "expand_mode": "none",
        "mode": "config",
        "path": "/ztp-fttb:ztp-fttb{1.1.1.1}",
        "th": th_id,
        "result_as": "json3"
    }
}
