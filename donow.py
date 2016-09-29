from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
	print request.headers
	return render_template("template.html")

@app.route("/authenticate", methods = ['POST'])
def authenticate():
	print request.headers
	print request.form #dictionary of args
	if (request.form['user'].lower() == "username" and request.form['pass'] == "password"):  #value of age
		return render_template("template2.html",match="are valid.")
	else:
		return render_template("template2.html",match="are invalid.")
		
if __name__ == "__main__":
	app.debug = True
	app.run()
	

	






