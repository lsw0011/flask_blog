from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlaalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '94fa092f521fc561151c4f5c313c0f6f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	username = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')



posts = [

	{
		'author' : 'Corey Schafer',
		'title': 'Blog Post 1',
		'content': 'first post content',
		'date_posted': 'April 20, 2018'
	},

	{
		'author' : 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'second post content',
		'date_posted': 'April 21, 2018'
	}

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts) #posts becomes available in the home.html template

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods = ['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == "admin@blog.com" and form.password.data == 'password':
			flash('you have been logged in!', 'success') 
			return redirect(url_for('home'))
		else: 
			flash('Login Unsuccessful. Please check email and password.', 'danger')
	return render_template('login.html', title = 'Login', form = form)

if __name__ == '__main__':
	app.run(debug=True)
