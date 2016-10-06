from flask import Flask, render_template, request, url_for, redirect
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
	
	if (request.form['auth'] == "login"):
		password = hashlib.sha1(request.form['pass']).hexdigest()
		print info[request.form['user']] + "\n"
		print password + "\n"
		
		if (request.form['user'].lower() in info and info[request.form['user']] == password):
				return render_template("template2.html",match="are valid.")
		else:
				return render_template("template2.html",match="are invalid." + info[request.form['user']] == password)

	else:
		if (request.form['user'].lower() not in info):
			x = open("data/info.txt",'a')
			x.write(request.form['user'].lower() + "," + hashlib.sha1(request.form['pass']).hexdigest() + "\n")
			return render_template("template2.html", match="have been registered")
		else:
			return render_temlate("template2.html", match="have been taken")
			
if __name__ == "__main__":
	app.debug = True
	app.run()
	

	






