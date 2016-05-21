from flask import Flask, render_template, request, session, redirect, flash
import re
from datetime import datetime
app = Flask(__name__)
app.secret_key = "adorable_beagles"

mail_val = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
num_check    = re.compile('[0-9]')
case_check = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])')

@app.route('/')                                                                                                                                                     
def submit_info():
  return render_template('index.html')  

@app.route('/process', methods=["POST"])
def validation():
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['email'] = request.form['email']
	session['pass'] = request.form['pass']
	session['confirm_pass'] = request.form['confirm_pass']


	if len(request.form['first_name']) < 1:
		flash('First Name cannot be empty!')
		return redirect('/')
	elif num_check.search(request.form['first_name']) != None:
		flash("First name can't have numbers")
		return redirect('/')
	elif len(request.form['last_name']) < 1:
		flash('Last Name cannot be empty!')
		return redirect('/')
	elif num_check.search(request.form['last_name']) != None:
		flash("Last name can't have numbers")
		return redirect('/')
	elif len(request.form['birthday']) < 1:
		flash('Date of birth cannot be empty!')
		return redirect('/')
	elif len(request.form['email']) < 1:
		flash['Email cannot be empty!']
	elif not mail_val.match(request.form['email']):
		flash('Your email is not valid!')
		return redirect('/')
	elif len(request.form['pass']) < 8:
		flash("Password cannot contain less than eight characters")
		return redirect('/')
	elif not case_check.match(request.form['pass']):
		flash("Password must contain at least one upper case and one lower case letter!")
		return redirect('/')
	elif len(request.form['confirm_pass']) < 8:
		flash("Password cannot contain less than eight characters")
		return redirect('/')
	elif request.form['pass'] != request.form['confirm_pass']:
		flash("Your passwords do not match!")
		return redirect('/')
  	else:
  		flash("Registration successful! Thank you!")
		return redirect('/')

if __name__ =="__main__":
	app.run(debug=True)