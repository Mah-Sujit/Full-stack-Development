from flask import Flask, jsonify, request

app = Flask(__name__)

businesses = [
    {
        'id': 1,
        'name': 'Costa Coffee',
        'town': 'London',
        "ratings": 4.5,
        "reviews": []
    },
    {
        'id': 2,
        'name': 'Starbucks',
        'town': 'Belfast',
        'ratings': 4.5,
        "reviews": []
    },
    {
        'id': 3,
        'name': 'Nero',
        'town': 'Manchester',
        'ratings': 4.5,
        "reviews": []
    }
]

@app.route('/', methods=['GET'])
def show_welcome():
    return jsonify({"message": "Welcome to Coffee Mart"})

@app.route('/businesses', methods=['GET'])
def show_businesses():
    return jsonify(businesses)

@app.route('/business/<int:business_id>', methods=['GET'])
def get_business(business_id):
    business = next((b for b in businesses if b['id'] == business_id), None)
    if business:
        return jsonify(business)
    return jsonify({"error": "Business not found"}), 404

if __name__ == '__main__':   # fixed _main_
        app.run(host="127.0.0.1", port=5055, debug=False, use_reloader=False)
