from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def root():
    return "<h1>Home Page</h1>"

@app.route("/users/<string:user_id>")
def get_user(user_id):
    user = {'id': user_id, 'name': "Test", "phone": 999343403}
    query = request.args.get('query')
    if query:
        user["query"] = query
    return jsonify(user), 200

@app.route('/users', methods=["POST"])
def create_user():
    data = request.get_json()
    status = {"status": "User created"}

    user = {"user": data}

    response_data = {**status, **user}

    return jsonify(response_data), 201


if __name__ == "__main__":
    app.run(debug=True, port=7000)


