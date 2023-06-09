from controller.blog import Blog


def blog_routes(api):
    api.add_resource(Blog, "/blog")
