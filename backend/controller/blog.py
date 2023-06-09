"""This file is for all Blog related logic behaviour"""
from utils.helper import is_a_duplicate
from flask_restful import Resource, reqparse

tasks = {1: "my new task", 2: "a really nice task", 3: "the best task"}

blog_post_args = reqparse.RequestParser()
blog_post_args.add_argument("task_id", type=int, help="The task_id is needed.")
blog_post_args.add_argument(
    "task_name", type=str, help="The task_name is required.", required=True
)


class Blog(Resource):
    """This Route is for the main blog requests"""

    def get(self):
        """
        This get method route will
        return all tasks stored in the list
        """
        return tasks, 200

    def post(self):
        """
        The post method route will if its not a duplicate
        adding the new task send via body to the list
        """
        args = blog_post_args.parse_args()
        task_name = args["task_name"]
        if not is_a_duplicate(item=task_name, collection=tasks.values()):
            new_task_id = max(tasks.keys()) + 1
            tasks[new_task_id] = task_name
            return {"task": tasks}, 201
        else:
            return {"Error": "task already in list."}, 400

    def put(self):
        """The put method route will update a task"""
        args = blog_post_args.parse_args()
        task_id = args["task_id"]
        task_name = args["task_name"]
        if task_id is None:
            return {"Error": "task_id is require for the change of an task."}, 400
        else:
            tasks[task_id] = task_name
            return tasks, 200
