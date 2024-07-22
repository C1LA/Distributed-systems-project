import unittest
from load_balancer import app

class LoadBalancerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_instances(self):
        response = self.app.post('/add', json={
            'n': 2,
            'hostnames': ['S1', 'S2']
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Added 2 instances', response.data)

    def test_remove_instances(self):
        response = self.app.delete('/rm', json={
            'n': 1,
            'hostnames': ['S1']
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Removed 1 instances', response.data)

    def test_route_request(self):
        response = self.app.get('/somepath')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'server', response.data)

if __name__ == '__main__':
    unittest.main()