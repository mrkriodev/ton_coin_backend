from flask import Flask
app = Flask(__name__)


@app.route('/api/user/balance')
def get_last_transaction():
    return "<h1>no balance</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
