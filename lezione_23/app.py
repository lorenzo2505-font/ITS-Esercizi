from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "<h3> hello world </h3>"

@app.route('/user/<string:username>/age/<int:age>')
def show_user_profile(username: str, age: int) -> str:
    return f'profilo di {username}, {age} anni'

@app.route('/post/<int:post_id>')
def show_post(post_id: int) -> str:
    return f'post {post_id}'

with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile', username='John Doe', age = 30))
    print(url_for('show_post', post_id=42))