"""This file is for all Blog related logic behaviour"""
from flask_restful import Resource, reqparse

posts = {
    1: {
        "post_title": "First Blog Post",
        "post_description": "This is the description of the first blog post.",
    },
    2: {
        "post_title": "Second Blog Post",
        "post_description": "This is the description of the second blog post.",
    },
    3: {
        "post_title": "Third Blog Post",
        "post_description": "This is the description of the third blog post.",
    },
}

blog_post_args = reqparse.RequestParser()
blog_post_args.add_argument("post_id", type=int)
blog_post_args.add_argument("post_title", type=str)
blog_post_args.add_argument("post_description", type=str)


class Blog(Resource):
    """This Route is for the main blog requests"""

    def __init__(self):
        self.args = blog_post_args.parse_args()
        self.post_id = self.args["post_id"]
        self.post_title = self.args["post_title"]
        self.post_description = self.args["post_description"]

    def get(self):
        """
        This get method route will
        return all tasks stored in the list.
        """
        return {"posts": posts}, 200

    def post(self):
        """
        The post method route will if its not a duplicate
        adding the new task send via body to the list.
        """
        if not all([self.post_title, self.post_description]):
            return {
                "Error": "You need a post_id, post_title, and post_description to create a post."
            }, 400

        if self.post_id in posts:
            return {"Error": "Post with that post_id already exists."}, 400

        if any(post["post_title"] == self.post_title for post in posts.values()):
            return {"Error": "Post with that post_title already exists."}, 400

        new_post_id = max(posts.keys()) + 1
        posts[new_post_id] = {
            "post_title": self.post_title,
            "post_description": self.post_description,
        }
        return {"posts": posts}, 201

    def put(self):
        """The put method route will update a task."""
        if self.post_id is None:
            return {
                "Error": "To change a post you are required to enter a post_id."
            }, 400

        if self.post_id not in posts:
            return {
                "Error": f"Post with that post_id: ({self.post_id}) does not exist."
            }, 400

        posts[self.post_id] = self.post_title
        return {"posts": posts}, 201

    def delete(self):
        """
        The delete method route will delete a task
        depending if the task_id even exists.
        """
        if self.post_id is None:
            return {"Error": "task_id is required for removing the task."}, 400

        if self.post_id not in posts:
            return {"Error": "Task with that task_id does not exist."}, 400

        del posts[self.post_id]
        return {"posts": posts}, 204
