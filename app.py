import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)

db = client.test

collection = db['flask-tutorial']

app = Flask(__name__)

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():

    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    data = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(data)

    return "To-Do Item Saved Successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
