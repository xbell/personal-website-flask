import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about-me')
def about_me():
    return render_template("about_me.html")

@app.route('/work-experience')
def work():
    return render_template("work_experience.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

if __name__ == '__main__':
    port = os.environ.get("PORT") or 5000
    app.run("0.0.0.0", port)
