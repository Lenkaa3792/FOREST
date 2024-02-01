from app import app, db, TreeSubmission

def seed_database():
    with app.app_context():
        # Seed the database with sample data
        submission = TreeSubmission(user_name='John Doe', tree_name='Oak', region='North', county='XYZ', trees_planted=20, phone_number='123456789')
        db.session.add(submission)
        db.session.commit()

if __name__ == "__main__":
    seed_database()
