import os
from controller.blog_controller import Blog
from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from models.blog_post import db

load_dotenv(".env")

# flask --app app.py --debug run
app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

db.init_app(app)

api.add_resource(Blog, "/blog")

if __name__ == "__name__":
    app.run(debug=True)
