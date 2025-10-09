from flask import Flask, url_for

app = Flask(__name__)

'''@app.route('/')
def home() -> str:
    return '<h3>hello world</h3>' '''


@app.route('/about')
def about() -> str:
    return '<p>questa applicazione è di prova ed è progettata da Lorenzo Acomanni, uno studente ITS che sta imparando a diventare un Full Stack Developer</p>'

@app.route('/user/<string:username>')
def user(username: str) -> str:
    return f'Benvenuto, {username}'

@app.route('/square/<int:n>')
def square(n: int) -> str:
    return f'{n**2}'

@app.route('/sum/<int:a>/<int:b>')
def somma(a: int, b: int) -> str:
    return f'{a + b}'

@app.route('/')
def show() -> str:
   return f"{url_for('about')}\n{url_for('user', username='popa')}\n{url_for('square', n=3)}\n{url_for('somma', a=1, b=5)}"




if __name__ == '__main__':
    
    app.run(debug = True)