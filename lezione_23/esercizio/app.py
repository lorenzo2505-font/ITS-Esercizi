from flask import Flask, url_for

app = Flask(__name__)

articles: dict = {1: 'bambino salva la madre da un incendio', 2: 'utente dice che windows è meglio di linux e utenti di arch linux gli svaligiano casa', 3: 'GTA 6 anticipato a domani'}

@app.route('/')
def home() -> str:
    return f'''

    <h2>link generici </h2>

    <a href={url_for("about")}>About</a> <br>
    <a href={url_for("user", username = "Atsu")}>User</a> <br>
    <a href={url_for("square", n = 5)}>Square</a> <br>
    <a href={url_for("somma", a = 20, b = 11)}>Sum</a>

    <h2> informazioni utenti </h2>
    
    <a href = {url_for("people", nome = "Marco", cognome = "Pierleoni", eta = 27, hobby = "fonico" )}>Primo Utente</a> <br>
    <a href = {url_for("people", nome = "Lorenzo", cognome = "Rossi", eta = 20, hobby = "linux" )}>Secondo Utente</a> <br>
    <a href = {url_for("people", nome = "Luca", cognome = "D'ambra", eta = 22, hobby = "rapine" )}>Terzo Utente</a> 

    <h2> Articoli <h2>

    <a href = {url_for('post', id = 1)}>Post</a>

    
    
    

    '''


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

@app.route('/people/<string:nome>/<string:cognome>/<int:eta>/<string:hobby>')
def people(nome: str, cognome: str, eta: int, hobby: str):
    return f"nome: {nome}, cognome: {cognome}, età: {eta}, hobby: {hobby}"

@app.route('/post/<int:id>/string:des')
def post(id: int) -> str:
    
    if id not in articles:
        return "trovato un baule d'oro ad ostia"
    
    return articles[id]






if __name__ == '__main__':
    
    app.run(debug = True)