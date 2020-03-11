# from unittest import TestCase
# from model import connect_to_db, db, example_data
# from server import app
# from flask import session

# class FlaskTestsBasic(TestCase):
#     """Flask tests."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         # Get the Flask test client
#         self.client = app.test_client()

#         # Show Flask errors that happen during tests
#         app.config['TESTING'] = True

#     def test_index(self):
#         """Test homepage page."""

#         result = self.client.get("/")
#         self.assertIn("Welcome", result.data)

# class FlaskTestsDatabase(TestCase):
#     """Flask tests that use the database."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         # Get the Flask test client
#         self.client = app.test_client()
#         app.config['TESTING'] = True

#         # Connect to test database
#         connect_to_db(app, "postgresql:///testdb")

#         # Create tables and add sample data
#         db.create_all()
#         example_data()

#     def tearDown(self):
#         """Do at end of every test."""

#         db.session.close()
#         db.drop_all()

#     def test_login(self):
#         """Test login page."""

#         result = self.client.post("/login",
#                                   data={"user_id": "rachel", "password": "123"},
#                                   follow_redirects=True)
#         self.assertIn("You are a valued user", result.data)
#                     #ToDo List for tests.py file:   
#     # need to test (add) - trip by location name
#     # need to test - (add) activities by location name
#     # need to test - (update) - trip by location name
#     # need to test - (update) - activities by location name
#     # need to test - (delete) - trip by location name
#     # need to test - (delete) - activity by location name
# class FlaskTestsLoggedIn(TestCase):
#     """Flask tests with user logged in to session."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         app.config['TESTING'] = True
#         app.config['SECRET_KEY'] = 'key'
#         self.client = app.test_client()

#         with self.client as c:
#             with c.session_transaction() as sess:
#                 sess['user_id'] = 1
                
# class FlaskTestsLoggedOut(TestCase):
#     """Flask tests with user logged in to session."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         app.config['TESTING'] = True
#         self.client = app.test_client()

#     def test_important_page(self):
#         """Test that user can't see important page when logged out."""

#         result = self.client.get("/important", follow_redirects=True)
#         self.assertNotIn("You are a valued user", result.data)
#         self.assertIn("You must be logged in", result.data)