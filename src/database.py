from pymongo import MongoClient

import private

class Database:

	collection = None

	def __init__(self, test = False):
		client = MongoClient("mongodb://{dbuser}:{dbpassword}@ds257848.mlab.com:57848/cloud_apps".format(dbuser = private.mongousername, dbpassword = private.mongopassword), connect = False)
		db = client.cloud_apps
		self.collection = db.peverywheretest if test else client.peverywhere
		data = { "name" : "haydenknapp", "age" : "21" }

	def destroy(self):
		self.collection.remove({})

	def add_user(self, username, fullname, password):
		data = { "_id" : username, "fullname" : fullname, "password" : password }
		self.collection.insert(data)

	def get_user(self, username):
		return self.collection.find_one({ "_id" : username })

	def user_exists(self, username):
		result = self.collection.find_one({ "_id" : username })
		return result != None
