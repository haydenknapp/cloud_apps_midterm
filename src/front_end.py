import random
import time
import json

from bson.json_util import dumps as bsonDumps
from bottle import template, run, route, request, response, get, post, redirect

from database import Database

db = Database(True)

logins = {}

@route('/')
def root():
	get_login()
	redirect('/posts')

def get_login(logout = False):
	cookie = request.get_cookie('login_token')
	if cookie not in logins:
		redirect('/login')
	if logout:
		logins.pop(cookie)
		redirect('/login')
	return logins[cookie]

@route('/createaccount')
def createaccount():
	message = request.params.message
	error = False
	if message == 'error':
		error = True
	return template('createaccount', error=error)

@route('/login')
def login():
	return template('login')

@route('/logout')
def logout():
	username = get_login(logout = True)

@post('/auth')
def auth():
	username = request.forms.username
	password = request.forms.password

	userInfo = db.get_user(username)
	
	if userInfo == None:
		redirect('/login')

	if password != userInfo['password']:
		redirect('/login')

	cookie = str(int(random.random() * 1000000000000))

	response.set_cookie('login_token', cookie)

	logins[cookie] = username

	redirect('/posts')

@post('/insertuser')
def insertuser():
	username = request.forms.username
	password = request.forms.password
	fullname = request.forms.fullname
	
	if db.user_exists(username):
		redirect('/createaccount?message=error')

	if len(username) < 1 or len(password) < 6:
		redirect('/createaccount?message=error')

	db.add_user(username, fullname, password)

	cookie = str(int(random.random() * 1000000000000))

	response.set_cookie('login_token', cookie)

	logins[cookie] = username

	redirect('/posts')

@route('/posts')
def posts_1():
	username = get_login()
	posts = db.get_posts_all()
	fullname = db.get_fullname(username)
#	for post in posts:
#		print(post)
	return template('main.tpl', posts=posts, fullname=fullname)

@post('/makepost')
def makepost():
	username = get_login()
	contents = request.forms.contents
	db.make_post(username, contents)
	redirect('/posts')

@post('/updatepost/<postid>')
def updatepost(postid):
	username = get_login()
	newContents = request.forms.newContents
	print(newContents)
	db.update_post(postid, newContents)
	redirect('/posts')
	

random.seed(time.time())
run(host='localhost', port='8080')
