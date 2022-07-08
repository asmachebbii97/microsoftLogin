import pickle
import re
from adal import AuthenticationContext
from flask import Flask, request, jsonify, render_template
from flask_ngrok import run_with_ngrok
from flask import Flask
from flask_cors import CORS,cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/*": {"origins": "*"}})
run_with_ngrok(app)


@app.route('/token')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def AzureAccessToken():
 
  
 
  username = 'asmachebbi@IPACT416.onmicrosoft.com'
  password = 'Asma789@'
  #authority = 'https://login.microsoftonline.com/ID secret client'
 
  authority = 'https://login.microsoftonline.com/eb01702c-abd2-44d6-93ad-49e7e183ba61'
  resource = 'https://analysis.windows.net/powerbi/api'
  clientId = 'ddca591b-7d94-43b9-b8e5-f3bc9e0dd408'
 
  if not authority.endswith('token'):
    regex = re.compile('^(.*[\/])')
    match = regex.match(authority)
    authority = match.group()
    authority = authority + username.split('@')[1]
 
  auth_context = AuthenticationContext(authority)

  token = auth_context.acquire_token_with_username_password(resource, username, password, clientId)
  
  
   
 
  return {
    "AzureToken":token["accessToken"]
    }
