from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tree_database.db'
db = SQLAlchemy(app)

class TreeSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
    tree_name = db.Column(db.String(50))
    region = db.Column(db.String(50))
    county = db.Column(db.String(50))
    trees_planted = db.Column(db.Integer)
    phone_number = db.Column(db.String(15))

# Move the db.create_all() inside the application context
with app.app_context():
    db.create_all()

# ... (rest of your code)

# Run the application if executed directly
if __name__ == "__main__":
    app.run(debug=True)
