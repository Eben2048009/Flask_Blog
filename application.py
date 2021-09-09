from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

application = Flask(__name__) 
application.config['SECRET_KEY'] = '8031b396580be80eed28e7178f0b40eb'


posts = [
    {
        'author': 'Eben Emmanuel',
        'title': 'Flask 101: An Introduction',
        'content': 'Getting Started with Flask',
        'date_posted': 'July 11 2021'
    },
    {
        'author': 'Mia Baslin Jolly',
        'title': 'Swimming and Karate',
        'content': 'Balancing all the tedious tasks each day',
        'date_posted': 'July 7 2021'
    }
]

@application.route('/')
@application.route('/home')
def home():
    return render_template('home.html', posts= posts)

@application.route('/about')
def about():
    return render_template('about.html', title= 'About')

@application.route('/register', methods= ['GET', 'POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')      ## Creating a Flash Message
        return redirect(url_for('home'))                                    ## If success then Redirect to home page
    return render_template('register.html', title= 'Register', form= form)

@application.route('/login')
def login():
    form= LoginForm()
    return render_template('login.html', title= 'Login', form= form)

if __name__ == '__main__':
    application.run(host= '127.0.0.1', port= 5000, debug = True)  
