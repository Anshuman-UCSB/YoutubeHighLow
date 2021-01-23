from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
import pyrebase

config = {
    "apiKey": "AIzaSyBpxGxnrTt-2YbfjRkEVVSoJ70PNBht_RQ",
    "authDomain": "ythighlow1.firebaseapp.com",
    "databaseURL": "https://ythighlow1-default-rtdb.firebaseio.com",
    "storageBucket": "ythighlow1.appspot.com",
    "projectId": "ythighlow1"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def getData():
    out = []
    for v in db.get().each():
        vals = v.val()
        out.append(((vals["channel"], vals["query"], vals["title"], vals["views"]),vals["thumbnail"]))

    return tuple(out)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

@app.route('/data')
def data():
    headers = ("channel","query","title","views","thumbnail")
    data = getData()
    # data = ()
    return render_template(
        "grid.html",
        headers = headers,
        data = data,
        title="Data",
        description="List of all sourced data."
    )



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)