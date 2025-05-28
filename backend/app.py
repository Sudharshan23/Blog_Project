# Entry Point

# Import Flask to create your web app.
# Import os to work with folder paths.
# Import the routes you made in routes.py.
from flask import Flask
import os
from routes import routes



# template_dir points to: ../frontend/templates — where your HTML files live.
# static_dir points to: ../frontend/static — where your CSS and JS live.
# These help Flask find your frontend files.
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend', 'static'))


#Create a Flask app and tell it:
#     * Where your templates are (index.html)
#     * Where your static files are (style.css, script.js)
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)


# Required for session support (used in login/logout)
app.secret_key = "your-very-secret-key"


# What it means:
#   * This connects the routes you wrote in routes.py into the main app.
#   * Now Flask knows about the /posts URL.
app.register_blueprint(routes)


# What it means:
#   * This tells Python: "If you're running this file directly, start the server!"
#   * debug=True makes Flask show errors when things go wrong (very helpful while learning).
if __name__ == "__main__":
    app.run(debug=True)
