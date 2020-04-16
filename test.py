from project import app
import unittest

class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response= tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        tester = app.test_client(self)
        response= tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    #ensure behaves correctly given correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username='admin', password='admin'), follow_redirects=True)
        self.assertIn(b'You were just logged in', response.data)

    #ensure behaves correctly given incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username='user', password='haslo'), follow_redirects=True)
        self.assertIn(b'Invalid credential.', response.data)

    #ensure logout behaves correctly
    def test_correct_logout(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(username='admin', password='admin'), follow_redirects=True)

        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You were just logged out', response.data)

    #ensure  that the main page requires login
    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response= tester.get('/', follow_redirects=True)
        self.assertTrue(b'You need to log in first.' in response.data)

    #ensure that post show up on the main page
    def test_post_show_up(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username='admin', password='admin'), follow_redirects=True)
        self.assertIn(b'hello from shell', response.data)


if __name__ == "__main__":
    unittest.main()