from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample initial list of shopping items
shopping_list = [
    {'id': 1, 'name': 'Milk', 'done': False},
    {'id': 2, 'name': 'Eggs', 'done': False},
    {'id': 3, 'name': 'Bread', 'done': True}
]

# Endpoint to retrieve all shopping items
@app.route('/api/shopping-list', methods=['GET'])
def get_shopping_list():
    return jsonify(shopping_list)

# Endpoint to add a new shopping item
@app.route('/api/shopping-list', methods=['POST'])
def add_shopping_item():
    new_item = {
        'id': shopping_list[-1]['id'] + 1,
        'name': request.json['name'],
        'done': False
    }
    shopping_list.append(new_item)
    return jsonify(new_item), 201

# Endpoint to update the status of a shopping item
@app.route('/api/shopping-list/<int:item_id>', methods=['PUT'])
def update_shopping_item(item_id):
    for item in shopping_list:
        if item['id'] == item_id:
            item['done'] = request.json['done']
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# Endpoint to delete a shopping item
@app.route('/api/shopping-list/<int:item_id>', methods=['DELETE'])
def delete_shopping_item(item_id):
    for item in shopping_list:
        if item['id'] == item_id:
            shopping_list.remove(item)
            return jsonify({'message': 'Item deleted'})
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
