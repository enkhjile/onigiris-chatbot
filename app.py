import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/webhook', methods=['GET'])
def verify():
    VERIFICATION_TOKEN = os.environ.get('VERIFICATION_TOKEN')
    print(VERIFICATION_TOKEN)
    token_sent = request.args.get('hub.verify_token')
    if token_sent == VERIFICATION_TOKEN:
        print('Verified!')
        return request.args.get('hug.challenge')
    return 'Invalid verification token!'


if __name__ == '__main__':
    app.run()
