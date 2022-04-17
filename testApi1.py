import requests


def get_fb_token(app_id, app_secret):
    url = 'https://graph.facebook.com/oauth/access_token'
    payload = {
        'grant_type': 'client_credentials',
        'client_id': app_id,
        'client_secret': app_secret
    }
    response = requests.post(url, params=payload)
    return response.json()['access_token']


print(get_fb_token(555, 1234))
