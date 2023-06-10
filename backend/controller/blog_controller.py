"""This file is for all Blog related logic behaviour"""
from flask_restful import Resource, reqparse
from models.blog_post import BlogPost


blog_post_args = reqparse.RequestParser()
blog_post_args.add_argument("post_id", type=int)
blog_post_args.add_argument("post_title", type=str)
blog_post_args.add_argument("post_description", type=str)


def check_for_post(valueName: str, value):
    new_posts_list = BlogPost.get_all()
    for post in new_posts_list:
        if post[valueName] == value:
            return True
    return False


class Blog(Resource):
    """This Route is for the main blog requests"""

    def __init__(self):
        self.args = blog_post_args.parse_args()
        self.post_id = self.args["post_id"]
        self.post_title = self.args["post_title"]
        self.post_description = self.args["post_description"]

    def get(self):
        """
        This get method will query all database post entrys and
        return them as a json like object.
        """
        return {"posts": BlogPost.get_all()}, 200

    def post(self):
        """
        The post method route will crea a new post if its not a duplicate
        post_id or post_title and if title and description are passed.
        """
        if not all([self.post_title, self.post_description]):
            return {
                "Error": "You need a post_title, and post_description to create a post."
            }, 400

        new_posts_list = BlogPost.get_all()

        if self.post_title in [post["post_title"] for post in new_posts_list]:
            return {"Error": "Post title already exists."}, 400

        try:
            new_post = BlogPost(
                title=self.post_title, description=self.post_description
            )
            new_post.save()
            return {"posts": new_posts_list}, 201
        except Exception as exc:
            raise RuntimeError("Failed to save the Blog Post Internal Error.") from exc

    def put(self):
        """The put method route will update a post."""

        # check if all needed parameters are set
        if self.post_id is None or not all([self.post_title, self.post_description]):
            return {
                "Error": "You need a post_id, post_title, and post_description to change a post."
            }, 400

        to_change_post = BlogPost.get_by_id(self.post_id)

        # Check if the post with the specified post_id not exists

        if not check_for_post("post_id", self.post_id) or to_change_post is None:
            return {"Error": f"Post with post_id ({self.post_id}) does not exist."}, 400

        # check if a post witht he same title already exists

        if check_for_post("post_title", self.post_title):
            return {
                "Error": f"Post with post_title ({self.post_title}) does already exist."
            }, 400

        to_change_post.post_title = self.post_title
        to_change_post.post_description = self.post_description
        to_change_post.update()

        new_posts_list = BlogPost.get_all()

        return {"posts": new_posts_list}, 201

    def delete(self):
        """
        The delete method route will delete a post
        depending if the post_id even exists.
        """
        if self.post_id is None:
            return {"Error": "The post_id is required for removing the post."}, 400

        if self.post_id not in posts:
            return {
                "Error": f"Post with that post_id: ({self.post_id}) does not exist."
            }, 400

        del posts[self.post_id]
        return {"posts": posts}, 200
