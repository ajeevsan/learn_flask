from flask import Flask

#! creating an object of the flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World"


if __name__ == "__main__":
    print("I'm inside under name now.")
    app.run(host='0.0.0.0', debug=True) 

