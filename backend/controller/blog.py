from flask_restful import Resource, reqparse

tasks = ["my new task", "a really nice task", "the best task"]

blog_post_args = reqparse.RequestParser()
blog_post_args.add_argument(
    "task_id", type=int, help="Error 400: The task_id is required.", required=True
)
blog_post_args.add_argument(
    "task_name", type=str, help="Error 400: The task_name is required.", required=True
)


class Blog(Resource):
    def get(self):
        return tasks, 200

    def post(self):
        args = blog_post_args.parse_args()
        task_name = args["task_name"]
        tasks.append(task_name)
        return {"task": tasks}
