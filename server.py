from flask import Flask, request
import aramark
app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
  credentials = request.get_json()

  return str(aramark.login(credentials['email'], credentials['password'])).replace("u'",'"').replace("'",'"')

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")