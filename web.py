from flask import Flask, render_template, request
import yelp_api
import os

app = Flask(__name__)

@app.route("/")
def index():
	address = request.values.get("address")
	terms = request.values.get("terms")
	recommendations = None
	top_3 = None
	if address:
		recommendations = yelp_api.get_businesses(address, terms)
		top_3 = recommendations[0:3]
	return render_template("index.html", recommendations=top_3, 
		address=address, terms=terms)

@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == "__main__":
	# port = int(os.environ.get("PORT", 5000))
	# app.run(host="0.0.0.0", port=port)
	app.run()