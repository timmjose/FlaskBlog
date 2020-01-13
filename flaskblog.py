
#imports Flask class, render_template is for the templates folder that can hold the HTML files, url_for is for connecting
#css to layout.html
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

#Python REPL: import secrets, secrets.token_hex(16)
app.config['SECRET_KEY'] = '6b22960aecf9b014ea39de366b493591'

#dummy data
posts = [
    {
        'author': 'Tim Santos',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Jan 9, 2020'
    },
        {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Jan 10, 2020'
    } 
]

#@app.route is pretty much where you route it in your website, ie:  localhost:5000/home = home page
#posts=posts lets the templates use the posts listed here, essentially the render template parameters are passed
#into the HTML file being called
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

#Lets you run DEBUG mode directly when you call the script ie: python flaskblog.py
#DEBUG mode is used so when you make changes and refresh localhost:5000 or http://127.0.0.1:5000/, it updates
#immediately without having to re run the server
if __name__ == '__main__':
    app.run(debug=True)