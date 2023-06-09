"""This file is for all Blog related logic behaviour"""
from utils.helper import is_a_duplicate
from flask_restful import Resource, reqparse

tasks = {1: "my new task", 2: "a really nice task", 3: "the best task"}

blog_post_args = reqparse.RequestParser()
blog_post_args.add_argument("task_id", type=int, help="The task_id is needed.")
blog_post_args.add_argument("task_name", type=str, help="The task_name is required.")


class Blog(Resource):
    """This Route is for the main blog requests"""

    def get(self):
        """
        This get method route will
        return all tasks stored in the list.
        """
        return {"tasks": tasks}, 201

    def post(self):
        """
        The post method route will if its not a duplicate
        adding the new task send via body to the list.
        """
        args = blog_post_args.parse_args()
        task_name = args["task_name"]
        if task_name is None:
            return {"Error": "task_name is required for adding a new task."}, 400
        elif is_a_duplicate(item=task_name, collection=tasks.values()):
            return {"Error": "task already in list."}, 400
        else:
            new_task_id = max(tasks.keys()) + 1
            tasks[new_task_id] = task_name
            return {"tasks": tasks}, 201

    def put(self):
        """The put method route will update a task."""
        args = blog_post_args.parse_args()
        task_id = args["task_id"]
        task_name = args["task_name"]
        if is_a_duplicate(item=task_name, collection=tasks.values()):
            return {"Error": "task already in list."}, 400
        elif task_id is None:
            return {"Error": "task_id is required for the change of an task."}, 400
        elif task_name is None:
            return {"Error": "task_name is required for a new task name."}, 400
        else:
            tasks[task_id] = task_name
            return {"tasks": tasks}, 201

    def delete(self):
        """
        The delete method route will delete a task
        depending if the task_id even exists.
        """
        args = blog_post_args.parse_args()
        task_id = args["task_id"]
        if task_id is None:
            return {"Error": "task_id is required for removing the task."}, 400
        elif task_id not in tasks:
            return {"Error": "Task with that task_id does not exist."}, 400
        else:
            del tasks[task_id]
            return {"tasks": tasks}, 201
