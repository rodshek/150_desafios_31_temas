from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Simulação de banco de dados
data_store = {}


class Item(Resource):
    def get(self, item_id):
        if item_id in data_store:
            return jsonify({item_id: data_store[item_id]})
        return jsonify({'message': 'Item not found'}), 404

    def post(self, item_id):
        if item_id in data_store:
            return jsonify({'message': 'Item already exists'}), 400
        data_store[item_id] = request.json.get('value')
        return jsonify({item_id: data_store[item_id]}), 201

    def put(self, item_id):
        if item_id not in data_store:
            return jsonify({'message': 'Item not found'}), 404
        data_store[item_id] = request.json.get('value')
        return jsonify({item_id: data_store[item_id]})

    def delete(self, item_id):
        if item_id in data_store:
            del data_store[item_id]
            return jsonify({'message': 'Item deleted'})
        return jsonify({'message': 'Item not found'}), 404


api.add_resource(Item, '/item/<string:item_id>')

if __name__ == '__main__':
    app.run(debug=True)
