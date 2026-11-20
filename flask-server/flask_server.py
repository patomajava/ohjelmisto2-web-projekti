from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="..", static_url_path="")

@app.route("/")
def index():
    return send_from_directory("..", "index.html")

@app.route("/pelaajan_tiedot")
def pelaajan_tiedot():
    return send_from_directory("..", "pelaajan_tiedot.html")

@app.route("/peli")
def peli():
    return send_from_directory("..", "peli.html")

@app.route("/tulokset")
def tulokset():
    return send_from_directory("..", "tulokset.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, use_reloader=True)
