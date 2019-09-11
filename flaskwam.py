
from flask import Flask
app = Flask(__name__)

@app.route("/tester")
def hello():
	return "Hello World!"

@app.route("/runner")
def goodbye():
	return "Running"

if __name__ == '__main__':
	app.run(debug=True)