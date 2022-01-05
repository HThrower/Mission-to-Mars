from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect
import scrape_mars
 

app = Flask(__name__)

# setup mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)



@app.route("/")
def index():
    print("I am on index.html")
    # write a statement that finds all the items in the db and sets it to a variable
    mars = mongo.db.mars.find_one()
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():     
    print("I am in scrape")
    mars = mongo.db.mars
    mars_data=scrape_mars.scrape_all()
    mars.insert_one(mars_data)
    #mars.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)