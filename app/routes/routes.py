from app.model.user import User
from app.model.article import Article
from app.model.comment import Comment

from app import db  # Assuming "db" is your SQLAlchemy instance
from flask import Blueprint, jsonify, request

article_bp = Blueprint('posts', __name__)


@article_bp.route('/articles/', methods=['GET'])
def get_articles():
    articles = Article.query.all()
    response = jsonify([article.serialize() for article in articles])
    return response, 200


@article_bp.route('/get/<int:article_id>', methods=['GET'])
def get_article(article_id):
    todo = Article.query.get(article_id)
    if todo is not None:
        response = jsonify(todo.serialize())
        return response, 200
    else:
        return jsonify({"message": "todo not found"}), 404


@article_bp.route('/delete/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    article = Article.query.get(article_id)  # Fetch the todo item by ID

    if article:
        db.session.delete(article)  # Delete the article item
        db.session.commit()  # Commit the changes to the database
        return jsonify({"message": "Article deleted successfully"}), 200
    else:
        return jsonify({"message": "Article not found"}), 404


# todo function return


@article_bp.route('/post', methods=['POST'])
def create():
    data = request.json  # Assuming you're sending JSON data in the request
    if not data:
        return jsonify({"error": "Invalid data"}), 400

    # todo voir vérification attribut
    new_article = Article(content=data['content'], completed=data['completed'])

    new_article = Article(
        user_id=data["user_id"],  # Assuming user_id is available in your context
        title=data['title'],  # Assuming 'title' is a key in the data dictionary
        content=data["content"]  # Assuming you want to set the current timestamp
    )

    db.session.add(new_article)
    db.session.commit()

    return jsonify({"message": "Article created successfully"}), 201


@article_bp.route('/put/<int:article_id>', methods=['PUT'])
def update(article_id):
    todo = Article.query.get(article_id)

    if todo is not None:
        data = request.json

        todo.content = data.get('content')
        todo.completed = data.get('completed')

        db.session.commit()

        response = jsonify({"message": "Todo updated successfully"})
        return response, 200
    else:
        return jsonify({"message": "Todo not found"}), 404

# class ClasseTest:
#     def __init__(self):
#         self.attribute = "valeur"
#
#     def methode_example(self):
#         return self.attribute
#
#
# def function_test(testo):
#     testo: ClasseTest = testo
#     print(testo.methode_example())
#
#
# test = ClasseTest()
# function_test(test)
