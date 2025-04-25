import unittest2
import app

class FlaskAppTest(unittest2.TestCase):
    def setUp(self):
        self.app = app.ai_app.test_client()

    def test_ask(self):
        response = self.app.get('/ask', json={'question': 'Hello?'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), response.get_json())

if __name__ == '__main__':
    unittest2.main()
