from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__) 
app.config['SECRET_KEY'] = '8031b396580be80eed28e7178f0b40eb'


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

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts= posts)

@app.route('/about')
def about():
    return render_template('about.html', title= 'About')


if __name__ == '__main__':
    app.run(host= '127.0.0.1', port= 5000, debug = True)  
