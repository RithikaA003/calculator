from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user}), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    user_id = max(users.keys(), default=0) + 1
    users[user_id] = data['name']
    return jsonify({'id': user_id, 'name': data['name']}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    users[user_id] = data['name']
    return jsonify({'id': user_id, 'name': data['name']}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        deleted_name = users.pop(user_id)
        return jsonify({'message': f'User {deleted_name} deleted'}), 200
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
