import requests
import json


def login(mail, password):
    s = requests.Session()
    payload = {
        'email': mail,
        'password': password
    }
    res = s.post('https://api.giggl.app/v1/auth', json=payload)
    s.headers.update({'autorization': json.loads(res.content)['token']})
    print(res.content)
    return s


session = login('devpycode@gmail.com', '123query')
r = session.patch('https://api.giggl.app/v1/users/@me', json = {'location': 'Sweden'})
print(r.content)