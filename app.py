from flask import Flask, request, jsonify, render_template, redirect
from random import choice
app = Flask(__name__)
import pyrebase

config = {
    "apiKey": "AIzaSyBpxGxnrTt-2YbfjRkEVVSoJ70PNBht_RQ",
    "authDomain": "ythighlow1.firebaseapp.com",
    "databaseURL": "https://ythighlow1-default-rtdb.firebaseio.com",
    "storageBucket": "ythighlow1.appspot.com",
    "projectId": "ythighlow1"
}

card1 = ("http://i3.ytimg.com/vi/mWnqMFgH4TM/hqdefault.jpg",
"Let's Play Minecraft Survival : Awesome New Adventure! Episode 1",
"fWhip",
251038)

card2 = ("http://i3.ytimg.com/vi/hSAJvWYZLY0/hqdefault.jpg",
"	Silencing Poker Twitter Trolls | VLOG 88",
"JohnnieVibes",
16693)
score = 0
best = 0

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def getData():
    out = []
    for v in db.get().each():
        vals = v.val()
        out.append(((vals["channel"], vals["query"], vals["title"], vals["views"]),vals["thumbnail"]))

    return tuple(out)
def grabCard():
    json = choice([v.val() for v in db.get().each()])
    return (json["thumbnail"],json["title"],json["channel"],json["views"])

# A welcome message to test our server
@app.route('/')
def index():
    return render_template("start.html")

@app.route('/data')
def data():
    headers = ("channel","query","title","views","thumbnail")
    data = getData()
    # data = ()
    return render_template(
        "grid.html",
        headers = headers,
        data = data
    )

@app.route('/play')
def game():
    global card1
    global card2
    card1 = grabCard()
    card2 = grabCard()
    #for a card:
    #(imgurl, title, channel name, viewcount)
    return render_template(
        "index.html",
        card1 = card1,
        card2 = card2,
        score=score
    )


@app.route('/api')
def api():
    global card1
    global card2
    global score
    sel = request.args.get("sel")
    sel = int("".join([x for x in sel if x.isnumeric()]))
    notsel = request.args.get("notsel")
    notsel = int("".join([x for x in notsel if x.isnumeric()]))
    correct = sel>=notsel
    print(sel)
    print(notsel)
    if(correct):
        print("RECOGNIZED CORRECT")
        score+=1
        card1 = card2
        card2 =grabCard()
    else:
        # redirect("/gameover")
        pass
    
    return {"correct": correct, "card1":card1, "card2":card2,"score":score}

@app.route("/gameover")
def gameover():
    global score
    global best
    best = max(score, best)
    outScore = score
    score = 0

    return render_template(
        "gameover.html",
        score=outScore,
        best=best
    )


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    # print(choice(grabCard()))
    app.run(threaded=True, port=5000)