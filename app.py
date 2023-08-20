from flask import Flask, render_template
import requests
from urllib.parse import urlencode
import base64
import webbrowser

app = Flask(__name__)
app.secret_key = 'jukestar'

client_id = "555f8c2403724d5f806815620d59bbd4"
client_secret = "055ad3da73b3428d96c2eae26d6a2032"
auth_code="AQAZKEwOxYuD9rEtmNx3LdTxD_tHFCneGBQQ0uiMKsw2sVpAZQJh81wxJGgYDBVTue7PGeuMje9tRTu9GiALElzpgJhRA3vJjg8_ElMO9orUCUw5kL2AWB2C_x9lbY5fEqCDekYcAImLFFzN9JA2BBUOZEddlco9VuWe3CV30hiF3jNuNVtz85KAovoZGMkDR63VNFo"
# token = "BQBtUhgUQ9vmv9qCSXretCuZkNOOypoVuffjVE-vjWU7dWfT2qXoC7dsJfxGgRns30w1U4io0rvIFecMMeTzbvM2aBhqnOU-1CuWO9GVnFB1C9GC4eq9VbBHiddFY5sn6zbSgnNPeuHnhgpN8rqGNIUQz9RDF0JhDGyyIC5r0Bf1VtxYh2pOEGwXqoJKVgEAkg1BAcu_Vjc87IPlJNM"

@app.route('/auth')
def authenticate():
    

    auth_headers = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": "http://localhost:5000/redirect",
        "scope": "user-library-read"
    }

    #webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))
    req = requests.get("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

@app.route('/get-token')
def get_token():
    encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

    token_headers = {
        "Authorization": "Basic " + encoded_credentials,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    token_data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": "http://localhost:5000/redirect"
    }

    req = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

    token = req.json()["access_token"]

    print(token)

    return render_template('output.html', output = token)

@app.route('/')
def index():    
    return render_template('index.html')