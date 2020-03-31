import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/webhooks', methods=['GET'])
def verify():
    VERIFICATION_TOKEN = os.environ.get('VERIFICATION_TOKEN')
    token_sent = request.args.get('hub.verify_token')
    if token_sent == VERIFICATION_TOKEN:
        print('Verified!')
        return request.args.get('hug.challenge')
    else:
        return 'Invalid verification token!'
