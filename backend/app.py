from flask import Flask
from flask_restful import Api
from routes.blog_routes import blog_routes

# flask --app app.py --debug run
app = Flask(__name__)
api = Api(app)

blog_routes(api=api)

if __name__ == "__name__":
    app.run(debug=True)
