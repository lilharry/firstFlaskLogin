from flask import Flask, render_template, request, url_for, redirect, session
import hashlib

app = Flask(__name__)

@app.route('/')
def hello():
	print request.headers
	return render_template("template.html")

@app.route("/authenticate", methods = ['POST'])
def authenticate():
	print request.headers
	print request.form #dictionary of args
	
	x = open("data/info.txt").readlines()
	info = {}
	
	for line in x:
		d = line.split(',')
		info[d[0]] = d[1].strip("\n")
	
	user = request.form['user'].lower()
	password = hashlib.sha1(request.form['pass']).hexdigest()
		
	
	if (request.form['auth'] == "login"):
		
		
		if (user in info):
			if (info[user] == password):
				return render_template("template2.html",match="You have logged in!")
			else:
				return render_template("template2.html",match="Your password is wrong.")
		else:
			return render_template("template2.html",match="Your username is wrong.")
			
	else:
		if (user not in info):
			x = open("data/info.txt",'a')
			x.write(user + "," + password + "\n")
			return render_template("template2.html", match="You have registered!")
		else:
			return render_template("template2.html", match="Your username has been taken.")
			
if __name__ == "__main__":
	app.debug = True
	app.run()
	

	






