from flask import Flask, render_template, request

from peliprojekti import main

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/peli_uusi", methods=["GET", "POST"])
def peli_uusi():

    if request.method == "POST":

        nimi = request.form.get("pelaajan_nimi")
        ika = request.form.get("pelaajan_ika")

        return render_template("/peli.html", nimi=nimi, ika=ika)

    return render_template("peli_uusi.html")

@app.route("/peli_lataa", methods=["GET", "POST"])
def peli_lataa():

    if request.method == "POST":

        tallennus = "valittu tallennus?"

        return render_template("/peli.html", tallennus=tallennus)

    return render_template("peli_lataa.html")

@app.route("/peli")
def peli():
    return render_template("peli.html")

@app.route("/tulokset")
def tulokset():
    return render_template("tulokset.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, use_reloader=True)
