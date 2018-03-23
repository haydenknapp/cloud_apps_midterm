import unittest

from database import Database

class TestDatabase(unittest.TestCase):
	def test_000_create_destroy(self):
		db = Database(True)
		db.destroy()

	def test_001_add_get_users(self):
		db = Database(True)

		db.add_user('hknapp4', 'Hayden Knapp', 'password1234!')
		result = db.get_user('hknapp4')
		self.assertEqual(result['fullname'], 'Hayden Knapp')
		self.assertEqual(result['password'], 'password1234!')

		self.assertTrue(db.user_exists('hknapp4'))
		self.assertFalse(db.user_exists('hknapp5'))

		db.destroy()

if __name__ == '__main__':
	unittest.main(verbosity = 2)
