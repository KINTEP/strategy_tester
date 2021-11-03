from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")

@app.route("/data")
def data():
	return render_template("dynamic.html")


if __name__ == "__main__":
	app.run(debug=True, port = 9000)

