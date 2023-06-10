import os
from flask import Flask
from flask_restful import Api
from routes.blog_routes import blog_routes
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv(".env")

# flask --app app.py --debug run
app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

db = SQLAlchemy(app)

blog_routes(api=api)

if __name__ == "__name__":
    app.run(debug=True)
