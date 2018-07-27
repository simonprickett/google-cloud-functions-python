import flask
import requests

def getUserDetails(request):
    user = requests.get('https://randomuser.me/api/').json()
    user = user['results'][0]
    user['generator'] = 'google-cloud-function'
    
    return flask.jsonify(user)