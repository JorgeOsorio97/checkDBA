base_url="http://64acdb529bb1.ngrok.io"


payload = {
    "status": "todo bien",
    "date": str(dt.now())
}
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", base_url + "/status", headers=headers, data=json.dumps(payload))
print(response)