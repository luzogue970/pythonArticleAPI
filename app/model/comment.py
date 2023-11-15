from app import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)
    content = db.Column(db.TEXT, nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'article_id': self.article_id,
            'content': self.content,
            'created_at': self.created_at
        }
