from flask import render_template, Flask

app = Flask(__name__)


@app.route("/users")
def user_list():
    users = [
        'Sovyak',
        'Gul',
        'Sovyak'
    ]

    return render_template(
        'user_list.html',
        users=users
    )


@app.route("/users/<string:username>")
def user(username):
    return render_template(
        'user.html',
        username=username,
    )







