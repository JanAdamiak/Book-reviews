from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

class RegisterForm(Form):
	username = StringField('Username', [validators.Length(min=4, max=20)])
	email = StringField('Email', [validators.Length(min=6, max=50)])
	password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords do not much.')])
	confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		render_template('index.html')
	return render_template('register.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)