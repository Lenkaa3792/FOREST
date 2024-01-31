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

@app.route("/", methods=["GET", "POST"])
def ussd():
    session_id = request.values.get("sessionId")
    user_input = request.values.get("text")

    # Check if this is the first interaction
    if not session_id:
        return "CON Welcome to the Tree Planting App!\nPlease enter your name:"

    # Split user input based on the USSD gateway response format
    user_input = user_input.split("*")

    # Handle user input based on the USSD menu
    if len(user_input) == 1:
        return "CON Enter your region:"

    elif len(user_input) == 2:
        return "CON Enter your county:"

    elif len(user_input) == 3:
        return "CON Enter the name of the tree(s) you planted:"

    elif len(user_input) == 4:
        return "CON Enter the number of trees planted:"

    elif len(user_input) == 5:
        return "CON Enter your phone number:"

    elif len(user_input) == 6:
        # Save user submission to the database
        name, region, county, tree_name, trees_planted, phone_number = user_input
        submission = TreeSubmission(user_name=name, tree_name=tree_name, region=region, county=county, trees_planted=int(trees_planted), phone_number=phone_number)
        db.session.add(submission)
        db.session.commit()

        return f"END Thank you, {name}! Your submission has been recorded."

if __name__ == "__main__":
    app.run(debug=True)
