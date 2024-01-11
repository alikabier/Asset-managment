import unittest
import requests

class TestAssetAPI(unittest.TestCase):
    def setUp(self):
        # Set up the Flask app for testing
        from api import app  # Replace 'your_flask_app' with the actual name of your Flask app file
        self.app = app.test_client()
        self.app.testing = True

    def test_add_asset(self):
        data = {
            "serial": "12345",
            "department": "IT",
            "asset": "Laptop",
            "quantity": 5,
            "cost": 1000,
            "supplier": "ABC Supplier",
            "campus": "Abbasia",
            "date": "2022-01-15"
        }

        response = self.app.post('/api/assets', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Asset added successfully')

    def test_get_all_assets(self):
        response = self.app.get('/api/assets')
        self.assertEqual(response.status_code, 200)

    def test_get_asset(self):
        serial_number = "12345"
        response = self.app.get(f'/api/assets/{serial_number}')
        self.assertEqual(response.status_code, 200)

    def test_update_asset(self):
        serial_number = "12345"
        data = {
            "quantity": 10,
            "cost": 1500
        }

        response = self.app.put(f'/api/assets/{serial_number}', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Asset updated successfully')

    def test_delete_asset(self):
        serial_number = "12345"
        response = self.app.delete(f'/api/assets/{serial_number}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Asset deleted successfully')

if __name__ == '__main__':
    unittest.main()
