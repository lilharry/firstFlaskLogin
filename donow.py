from flask import Flask, render_template, request, url_for, redirect, session
import hashlib
from utils import functions
import os.path

app = Flask(__name__)

if os.path.isfile('data/secretkey.txt'):
	app.secret_key = open('data/secretkey.txt').readline().strip('\n')


	
@app.route('/')
def hello():
	if 'username' in session:
		return render_template("welcome.html",welcomed=session['username'])
	return render_template("login.html")

@app.route("/authenticate", methods = ['POST'])
def authenticate():
	print request.headers
	print request.form #dictionary of args
		
	info = functions.genDic()
	
	user = request.form['user'].lower()
	password = hashlib.sha1(request.form['pass']).hexdigest()
		
	
	if (request.form['auth'] == "login"):
		if (user in info):
			if (info[user] == password):
				session['username'] = user
				return render_template("welcome.html",welcomed=user)
			else:
				return render_template("error.html",match="Your password is wrong.")
		else:
			return render_template("error.html",match="Your username is wrong.")
	else:
		if (user not in info):
			functions.write(user,password)
			return render_template("error.html", match="You have registered!")
		else:
			return render_template("error.html", match="Your username has been taken.")
		
@app.route("/logout")
def logout():
	session.pop('username')
	return redirect(url_for('hello'))
		
if __name__ == "__main__":
	app.debug = True
	app.run()
	

	






