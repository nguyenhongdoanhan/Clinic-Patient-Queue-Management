import json, urllib.request
url='http://127.0.0.1:8080/api/patients/1'
data={
  'full_name':'Test User',
  'gender':'Nam',
  'birthday':'1991-02-02',
  'phone':'0912345678',
  'email':'test.user@example.com',
  'address':'Da Nang'
}
req=urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type':'application/json'}, method='PUT')
with urllib.request.urlopen(req) as r:
    print(r.getcode())
    print(r.read().decode())
