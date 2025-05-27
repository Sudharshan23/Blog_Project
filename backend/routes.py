# URL routes

#importing flask and tools from flask like 
# blueprint (lets us seperate routes into different files)
# render_templates (allows python to send data to an HTML file)
from flask import Blueprint, render_template


# Think of a Blueprint like a small app inside your big app.
# This line creates a group of routes called "routes"
routes = Blueprint("routes", __name__)


# I am creating a list of (Fake) blog posts
# Each post is a dictonary with title and author.
posts = [
    {"title": "Getting Started with Python", "author": "Sudharshan"},
    {"title": "Flask for Beginners", "author": "AI Buddy"},
    {"title": "How to Hack Ethically", "author": "Cyber Cat"}
]


# @routes.route("/posts"): this creates a route → http://localhost:5000/posts
# When someone visits /, Flask will:
#    * Run the hompage() function
#    * Send the posts list to index.html using render_template()
@routes.route("/")
def hompage():
    return render_template("index.html", posts=posts)