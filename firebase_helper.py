import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

tweet_keys = ['id', 'url', 'verified', 'images', 'timestamp', 'text', 'links', 'isQuote', 'isRetweet', 'likes', 'replies', 'retweets', 'quotes', 'searchQuery', 'user']

# doc_ref = db.collection("users").document("alovelace")
# doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})
async def upload_tweet(tweet):
    # print(tweet.keys())
    tweet_json = {"id": tweet["id"], "url": tweet["url"], "timestamp": tweet["timestamp"], "text": tweet["text"], "isQuote": tweet["isQuote"], "isRetweet": tweet["isRetweet"], "likes": tweet["likes"], "replies": tweet["replies"], "retweets": tweet["retweets"], "quotes": tweet["quotes"], "user": tweet["user"]}
    
    if ("images" in tweet.keys()):
        tweet_json["images"] = tweet["images"]
        # print("added images")

    tweet_id = tweet["id"]
    doc_ref = db.collection("tweets").document(tweet_id)
    doc_ref.set(tweet_json)

async def get_last_run_id():
    doc_ref = db.collection("runs").document("last")
    doc = doc_ref.get()
    return doc.to_dict()["id"]

async def set_last_run_id(id):
    doc_ref = db.collection("runs").document("last")
    doc_ref.set({"id": id})