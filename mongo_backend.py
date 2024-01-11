from pymongo import MongoClient

class MongoBackend:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['asset_management']
        self.asset_collection = self.db['assets']

    def add_asset(self, data):
        self.asset_collection.insert_one(data)

    def get_all_assets(self):
        return list(self.asset_collection.find())

    def get_asset_by_serial(self, serial):
        return self.asset_collection.find_one({"serial": serial})

    def update_asset_by_serial(self, serial, data):
        self.asset_collection.update_one({"serial": serial}, {"$set": data})

    def delete_asset_by_serial(self, serial):
        self.asset_collection.delete_one({"serial": serial})
