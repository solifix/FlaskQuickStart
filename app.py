from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/bye")
def bye_world():
    return "<p>Bye, World!</p>"


@app.route("/posts")
def posts():
    return render_template('posts.html', posts=range(1, 11))


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


@app.route("/hello/<username>")
def hello_user(username):
    return render_template('hello_user.html', username=username)


@app.route('/login')
def login():
    return 'login'
