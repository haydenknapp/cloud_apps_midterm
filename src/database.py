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
		self.collection.delete_many({})

	def add_user(self, username, fullname, password):
		data = { "_id" : username, "fullname" : fullname, "password" : password }
		self.collection.insert_one(data)

	def get_user(self, username):
		return self.collection.find_one({ "_id" : username })

	def user_exists(self, username):
		result = self.collection.find_one({ "_id" : username })
		return result != None

	def make_post(self, username, contents):
		return self.collection.insert_one({ "author" : username, "contents" : contents })

	def get_posts_all(self):
		return self.collection.find( { "author" : { "$exists" : "true" } } )

	def get_fullname(self, username):
		return self.collection.find_one( { "_id" : username } )['fullname']

	def update_post(self, _id, newContents):
		self.collection.update_one({ '_id' : _id }, { '$set' : { 'contents' : newContents }}) 
