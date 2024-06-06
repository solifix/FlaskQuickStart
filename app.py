from flask import render_template, request, redirect, url_for, session
from flask import Flask

app = Flask(__name__)

user_database = {
    "sofia": "221133",
    "solomia": "123456",
    "eva": "654321",

}

app.secret_key = 'jhu5436hgvgbf'


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in user_database and user_database[username] == password:
            session['username'] = username

            return redirect(
                url_for('user', username=request.form['username'])
            )

    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route("/users/<username>")
def user(username):
    if 'username' in session and session['username'] == username:
        return render_template(
            'user.html',
            username=username
        )


@app.route('/users')
def users():
    users = [
        'kyznetsov',
        'arsen',
        'Sovyak'
    ]
    return render_template('users.html', users=users)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
