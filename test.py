from unittest import TestCase

from app import app
from model import db, User

# Use test database and don't clutter tests with SQL
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///bdayGame"
app.config['SQLALCHEMY_ECHO'] = False


app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

app.config['WTF_CSRF_ENABLED'] = False

db.drop_all()
db.create_all()


def test_welcome(self):
    with app.test_client() as client:
        # can now make requests to flask via `client`
        resp = client.get('/welcome')
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('<h1>WELCOME TO THE BIRTHDAY GAME!!</h1>', html)

def test_newgame(self):
    with app.test_client() as client:
        # can now make requests to flask via `client`
        resp = client.get('/newgame')
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('<h2>In the last year...</h2>', html)
        
def test_index(self):
    with app.test_client() as client:
        # can now make requests to flask via `client`
        resp = client.get('/')
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('<h1>Birthday Game</h1>', html)
        
class UserViewsTestCase(TestCase):
    """Tests for views for Users."""

    def setUp(self):
        """Make demo data."""

        User.query.delete()

        user = User(name="Test User", email="test@test.com")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        """Clean up fouled transactions."""

        db.session.rollback()
        
        