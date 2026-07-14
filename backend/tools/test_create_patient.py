import json
import urllib.request

url = 'http://127.0.0.1:8080/api/patients'
data = {
    'full_name': 'Test User',
    'gender': 'Nam',
    'birthday': '1990-01-01',
    'phone': '0912345678',
    'email': 'test.user@example.com',
    'address': 'Da Nang'
}

req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
with urllib.request.urlopen(req) as r:
    print('STATUS', r.getcode())
    print(r.read().decode())
