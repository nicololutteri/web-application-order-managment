import requests

def getToken(username, password):
    r = requests.post('http://webuserend:50100/login/' + username + '/', data = { 'password': password })
    
    if (r.status_code == 200):
        return r.json()['token']
    else:
        raise
