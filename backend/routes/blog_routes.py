"""This file will be responsible for all route depending for the blog part"""
from controller.blog import Blog


def blog_routes(api):
    """This method will add the endpoint to the resful api"""
    api.add_resource(Blog, "/blog")
