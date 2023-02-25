from flask import Flask, render_template

#! creating an object of the flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')


if __name__ == "__main__":
    print("I'm inside under name now.")
    app.run(host='0.0.0.0', debug=True) 

