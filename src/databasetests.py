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
		self.assertEqual(db.get_fullname('hknapp4'), 'Hayden Knapp')

		db.destroy()

	def test_002_add_get_posts(self):
		db = Database(True)

		post1Contents = "This is the first post."
		post2Contents = "This is the second post."

		db.make_post('hknapp4', post1Contents)
		db.make_post('hknapp4', post2Contents)

		db.destroy()

	def test_003_update_post(self):
		db = Database(True)

		db.add_user('hknapp4', 'Hayden Knapp', 'password1234!')
		post1Contents = "This is the first post."
		post2Contents = "This is the second post."

		db.make_post('hknapp4', post1Contents)
		db.make_post('hknapp4', post2Contents)

		posts = db.get_posts_all()
		for post in posts:
			print(post)
			db.update_post(post['_id'], 'New Contents')
		posts = db.get_posts_all()
		for post in posts:
			print(post)

		db.destroy()

if __name__ == '__main__':
	unittest.main(verbosity = 2)
