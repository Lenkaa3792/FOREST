from flask import Flask, jsonify, request
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

@app.route("/get_report", methods=["GET"])
def get_report():
    # Fetch data from the database (example: get the total number of trees planted)
    total_trees_planted = TreeSubmission.query.with_entities(db.func.sum(TreeSubmission.trees_planted)).scalar()

    return jsonify({"total_trees_planted": total_trees_planted})

@app.route("/get_submissions", methods=["GET"])
def get_submissions():
    # Fetch all submissions from the database
    submissions = TreeSubmission.query.all()

    # Convert submissions to a list of dictionaries
    submissions_list = [{"user_name": submission.user_name,
                         "tree_name": submission.tree_name,
                         "region": submission.region,
                         "county": submission.county,
                         "trees_planted": submission.trees_planted,
                         "phone_number": submission.phone_number} for submission in submissions]

    return jsonify({"submissions": submissions_list})

if __name__ == "__main__":
    app.run(debug=True)
