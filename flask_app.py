from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Cyber Masters Network.html")

@app.route("/privacypolicy")
def privacypolicy():
    return render_template("Privacy Policy.html")

if __name__ == "__flask_app__":
    app.run(debug=True)