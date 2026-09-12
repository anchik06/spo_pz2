from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/places")
def places():
    return render_template("places.html")

@app.route("/program")
def program():
    return render_template("program.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/decor")
def decor():
    return render_template("decor.html")

@app.route("/changelog")
def changelog():
    return render_template("changelog.html")

if __name__ == "__main__":
    app.run(debug=True)
