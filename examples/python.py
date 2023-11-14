#! /usr/bin/env python3

import os, requests

infura_key = os.environ["INFURA_KEY"]
keys = requests.post("https://mainnet.infura.io/v3/" + infura_key, json={
    "jsonrpc": "2.0",
    "method": "eth_call",
    "params": [{
        "to": "0x000000000774019b96f067cda9fE26076649c729",
        "data": "0x0f560cd7"
    }, "latest"],
    "id": 0
}).json()["result"][130:]
result = {}
for i in range(0, len(keys), 64):
    address = "0x" + requests.post("https://mainnet.infura.io/v3/" + infura_key, json={
        "jsonrpc": "2.0",
        "method": "eth_call",
        "params": [{
            "to": "0x000000000774019b96f067cda9fE26076649c729",
            "data": "0x21f8a721" + keys[i:i+64]
        }, "latest"],
        "id": 0
    }).json()["result"][26:]
    key = bytes.fromhex(keys[i:i+64]).replace(b"\x00", b"").decode("ascii")
    result[key] = address
print(result)
