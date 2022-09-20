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
 
  
 
  username = 'asmachebbi@ipact219.onmicrosoft.com'
  password = 'Asma789@'
  #authority = 'https://login.microsoftonline.com/ID secret client'
 
  authority = 'https://login.microsoftonline.com/13F8Q~YrS5B2T46HJEui69vMcPAgRWCFb4KZoc6p'
  resource = 'https://analysis.windows.net/powerbi/api'
  clientId = '744d3136-12dc-4030-ae2f-0c04f6e33e99'
 
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
