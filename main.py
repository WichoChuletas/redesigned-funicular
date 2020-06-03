from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    return 'Hello World Flask, your IP is {}'.format(user_ip)



