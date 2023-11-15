from flask import Flask
from flask_cors import CORS
from app.routes.routes import article_bp
from app import db
from waitress import serve

app = Flask(__name__)
app.register_blueprint(article_bp)

# Allow all origins for demonstration purposes.
# You should restrict this to specific origins in production.
cors = CORS(app, resources={r"*": {"origins": "*"}})

localUrl = 'mysql+pymysql://root:todo@localhost/news_paper'
dockerUrl = 'mysql+pymysql://root:todo@db/news_paper'

app.config['SQLALCHEMY_DATABASE_URI'] = localUrl

if __name__ == 'main':
    with app.app_context():
        db.create_all()
    app.json.sort_keys = False
    app.run()

with app.app_context():
    db.init_app(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
    # serve(app, host="0.0.0.0", port=5001)

