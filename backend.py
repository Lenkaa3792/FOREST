from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forest_ussd.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class TreeSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), nullable=False)
    tree_name = db.Column(db.String(255), nullable=False)
    region = db.Column(db.String(255), nullable=False)
    county = db.Column(db.String(255), nullable=False)
    trees_planted = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

# Create the table within an application context
with app.app_context():
    db.create_all()

# Route to get all tree submissions
@app.route('/get_submissions')
def get_submissions():
    submissions = TreeSubmission.query.all()
    result = []
    for submission in submissions:
        result.append({
            'user_name': submission.user_name,
            'tree_name': submission.tree_name,
            'region': submission.region,
            'county': submission.county,
            'trees_planted': submission.trees_planted,
            'phone_number': submission.phone_number
        })
    return jsonify(result)

# Route to submit tree information
@app.route('/submit_tree', methods=['POST'])
def submit_tree():
    data = request.json
    new_submission = TreeSubmission(
        user_name=data['user_name'],
        tree_name=data['tree_name'],
        region=data['region'],
        county=data['county'],
        trees_planted=data['trees_planted'],
        phone_number=data['phone_number']
    )
    db.session.add(new_submission)
    db.session.commit()
    return jsonify({'message': 'Tree submission successful'})

if __name__ == '__main__':
    app.run(debug=True)
