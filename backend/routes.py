# URL routes

#importing flask and tools from flask like 
# blueprint (lets us seperate routes into different files)
# render_templates (allows python to send data to an HTML file)
from flask import Blueprint, render_template, request, redirect, url_for, session


# Think of a Blueprint like a small app inside your big app.
# This line creates a group of routes called "routes"
routes = Blueprint("routes", __name__)


# I am creating a list of (Fake) blog posts
# Each post is a dictonary with title and author.
# check from the "/new-post"
posts = []


# fake credentials
USERNAME = "admin"
PASSWORD = "sudhar123@"



# @routes.route("/posts"): this creates a route → http://localhost:5000/posts
# When someone visits /, Flask will:
#    * Run the hompage() function
#    * Send the posts list to index.html using render_template()
#  We are initiating a login session. so this IF Else is for-
#  whenever i login with my username and password the lists will show or else 
# posts=[] (shows the empty list)
# This is step 1
@routes.route("/")
def hompage():
    if session.get("logged_in"):
        return redirect(url_for("routes.dashboard"))
    return render_template("index.html")
    
    


# This is step 2 (logging in with username and password)
# this is login form submission.
# this is checking if the USERNAME and PASSWORD are matching to the ones that i gave
# here if it is matching it will go to thhe routes.hompage function and execute and display the posts

@routes.route("/login",methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        session["logged_in"] = True
        return redirect(url_for("routes.hompage"))
    else:
        return "<h3> Invalid Credentials. <a href ='/'> Try Again </a></h3>"
    
# last function is to logout
@routes.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("routes.hompage"))


# after logging in with credentials showing all the posts (my Dashboard)
#afte logging in it takes us to http://localhost:5000/dashboard  from http://localhost:5000
# checks whether in am logged in or not using "logged_in" thats why i have given if not condition
# if the user is not logged in it will take him to hompage not My Dashboard
# if the user is logged in he will he taken to dashboard.html and the contents will be displayed
@routes.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("routes.hompage"))
    return render_template("dashboard.html", posts=posts)


# after logging iadding new posts
# This defines a POST route for creating new posts.
# It will be triggered when a user submits the "New Post" form on dashboard.html.
# Again, checks if the user is logged in. If not, send them back to the homepage.
# Gets the value of the form field named title.
# Gets the value of the form field named content.
# Adds the new post (as a dictionary) to the posts list.
# fter adding the new post, redirects the user back to the dashboard so they can see the updated list.
@routes.route("/new-posts", methods=["POST"])
def new_post():
    if not session.get("logged_in"):
        return redirect(url_for("routes.hompage"))
    title = request.form.get("title")
    content = request.form.get("content")
    posts.append({"title": title, "content": content})
    return redirect(url_for("routes.dashboard"))



#createed a new html page for new-posts
@routes.route("/new-posts", methods=["GET"])
def new_post_page():
    if not session.get("logged_in"):
        return redirect(url_for("routes.homepage"))
    return render_template("new-posts.html")


# creating a new html page for viewing the Post detailed way
# View individual post
@routes.route("/post/<int:post_id>")
def view_post(post_id):
    if not session.get("logged_in"):
        return redirect(url_for("routes.homepage"))
    if post_id >= len(posts):
        return "Post not found", 404
    post = posts[post_id]
    return render_template("view-post.html", post=post)

# Edit post page
@routes.route("/edit-post/<int:post_id>")
def edit_post_page(post_id):
    if not session.get("logged_in"):
        return redirect(url_for("routes.homepage"))
    if post_id >= len(posts):
        return "Post not found", 404
    post = posts[post_id]
    return render_template("edit-post.html", post=post, post_id=post_id)

# Update post after editing
@routes.route("/update-post/<int:post_id>", methods=["POST"])
def update_post(post_id):
    if not session.get("logged_in"):
        return redirect(url_for("routes.homepage"))
    title = request.form.get("title")
    content = request.form.get("content")
    posts[post_id] = {"title": title, "content": content}
    return redirect(url_for("routes.dashboard"))

# Delete post
@routes.route("/delete-post/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    if not session.get("logged_in"):
        return redirect(url_for("routes.homepage"))
    if post_id < len(posts):
        posts.pop(post_id)
    return redirect(url_for("routes.dashboard"))

