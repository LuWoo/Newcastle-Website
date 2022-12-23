from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': "Luke",
        'title': 'First Post',
        'content': 'lots of text',
        'date_posted': '22nd November 2022'
    },
    {
        'author': "Bob",
        'title': 'Last Post',
        'content': 'Loads of Words',
        'date_posted': '23rd December 2022'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')