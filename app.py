from flask import Flask, render_template

#! creating an object of the flask
app = Flask(__name__)

sample_dict = [
    {
        'id': 1,
        'name': 'Sanjeev',
        'age': 24
    },
    {
        'id': 2,
        'name': 'Subham',
        'age': 24
    },
    {
        'id': 3,
        'name': 'Kabir',
        'age': 24
    }
]


@app.route("/")
def hello_world():
    return render_template('home.html', data=sample_dict)


if __name__ == "__main__":
    print("I'm inside under name now.")
    app.run(host='0.0.0.0', debug=True)
