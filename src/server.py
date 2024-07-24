from flask import Flask, jsonify, request,send_file

def create_app(enviroment):
    app = Flask(__name__)
    return app

app = create_app("a")

@app.route('/my-first-api', methods = ['GET'])
def hello():
    name = request.args.get('name')
    if name is None:
        text = 'Hola!'
    else:
        text = 'Hola ' + name + '!'
    return text


if __name__ == '__main__':
    app.run(debug=True, port=7000)