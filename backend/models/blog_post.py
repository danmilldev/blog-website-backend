from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(100), nullable=False)
    post_description = db.Column(db.String(255), nullable=False)

    def __init__(self, title, description):
        self.post_title = title
        self.post_description = description

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        all_posts = BlogPost.query.all()
        posts_dict = [
            {
                "post_id": post.id,
                "post_title": post.post_title,
                "post_description": post.post_description,
            }
            for post in all_posts
        ]
        return posts_dict

    @staticmethod
    def get_by_id(post_id):
        return BlogPost.query.filter_by(id=post_id).first()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
