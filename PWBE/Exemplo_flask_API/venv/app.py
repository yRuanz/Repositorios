from flask import Flask, jsonify, request

app = Flask(__name__)

user = {
    "nome" : "Carlos",

    "Idade" :  "23",

    "Cidade" : "Jundiai"   }

@app.route('/', methods=['GET'])
def index():
    return jsonify(user)

@app.route('/', methods=['GET'])
def index():
    return 'Hello, world!'

@app.route('/user', methods=['POST'])
def login():
    item = request.json
    userList.append(item)
    return userList

if __name__ == '__main__':
    app.run(host="0.0.0.0")