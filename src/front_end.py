import random
import time

from bottle import template, run, route, request, response, get, post, redirect

from database import Database

db = Database(True)

logins = {}

def get_login(logout = False):
	cookie = request.get_cookie('login_token')
	if cookie not in logins:
		redirect('/login')
	if logout:
		logins.pop(cookie)
		redirect('/login')
	return logins[cookie]

@route('/')
def root():
	get_login()
	return 'Hello!'

@route('/createaccount')
def createaccount():
	return template('createaccount')

@route('/login')
def login():
	db = Database()
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

	redirect('/home/{}'.format(username))

@post('/insertuser')
def insertuser():
	username = request.forms.username
	password = request.forms.password
	fullname = request.forms.fullname
	
	if db.user_exists(username):
		redirect('/createaccount')

	if len(username) < 1 or len(password) < 6:
		redirect('/createaccount')

	db.add_user(username, fullname, password)

	cookie = str(int(random.random() * 1000000000000))

	response.set_cookie('login_token', cookie)

	logins[cookie] = username

	redirect('/home/{}'.format(username))

@route('/home/<username>')
def home(username):
	get_login()
	return username

random.seed(time.time())
run(host='localhost', port='8080')
