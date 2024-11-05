import hmac
import base64
import time
from pybitapi.variables import *

def parse_params_to_str(data):
    url = '?'
    for key, value in data.items():
        url = url + str(key) + '=' + str(value) + '&'

    return url[0:-1]

def get_timestamp():
    return int(time.time() * 1000)

def pre_hash(timestamp, method, request_path, body):
    return str(timestamp) + str.upper(method) + str(request_path) + str(body)

def sign(message, secret_key):
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    dig = mac.digest()
    return base64.b64encode(dig)

def get_header(api_key, sign, timestamp, passphrase):
    header = dict()
    header[CONTENT_TYPE] = APPLICATION_JSON
    header[ACCESS_KEY] = api_key
    header[ACCESS_SIGN] = sign
    header[ACCESS_TIMESTAMP] = str(timestamp)
    header[ACCESS_PASSPHRASE] = passphrase

    return header