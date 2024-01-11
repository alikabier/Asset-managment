from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from mongo_backend import MongoBackend

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/asset_management'
mongo = PyMongo(app)
mongo_backend = MongoBackend()

# API endpoint to add a new asset
@app.route('/api/assets', methods=['POST'])
def add_asset():
    data = request.get_json()
    mongo_backend.add_asset(data)
    return jsonify({"message": "Asset added successfully"}), 201

# API endpoint to get all assets
@app.route('/api/assets', methods=['GET'])
def get_all_assets():
    assets = mongo_backend.get_all_assets()
    return jsonify({"assets": assets}), 200

# API endpoint to get a specific asset by serial number
@app.route('/api/assets/<serial>', methods=['GET'])
def get_asset(serial):
    asset = mongo_backend.get_asset_by_serial(serial)
    return jsonify({"asset": asset}), 200 if asset else 404

# API endpoint to update an asset by serial number
@app.route('/api/assets/<serial>', methods=['PUT'])
def update_asset(serial):
    data = request.get_json()
    mongo_backend.update_asset_by_serial(serial, data)
    return jsonify({"message": "Asset updated successfully"}), 200

# API endpoint to delete an asset by serial number
@app.route('/api/assets/<serial>', methods=['DELETE'])
def delete_asset(serial):
    mongo_backend.delete_asset_by_serial(serial)
    return jsonify({"message": "Asset deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
