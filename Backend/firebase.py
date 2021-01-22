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


def pushJson(dat):
    db.push(dat)
    

if __name__ == "__main__":
    pass    