from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# GET endpoint to retrieve users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST endpoint to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
