import unittest
from server import app

class ServerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Server is running', response.data)

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'healthy', response.data)

    def test_process_request(self):
        response = self.app.post('/process', json={'key': 'value'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Data processed', response.data)
        self.assertIn(b'"key": "value"', response.data)

if __name__ == '__main__':
    unittest.main()