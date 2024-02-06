from backend import app, db, TreeSubmission

def seed_database():
    # Create an application context
    with app.app_context():
        # Create database tables
        db.create_all()

        # Seed data
        submissions_data = [
            {
                'user_name': 'John Doe',
                'phone_number': '123456789',
                'county': 'XYZ',
                'region': 'North',
                'tree_name': 'Oak',
                'trees_planted': 20,
            },
            {
                'user_name': 'Jane Smith',
                'phone_number': '987654321',
                'county': 'ABC',
                'region': 'South',
                'tree_name': 'Maple',
                'trees_planted': 15,
            },
            # Add more submissions as needed
        ]

        # Add submissions to the session
        for data in submissions_data:
            submission = TreeSubmission(**data)
            db.session.add(submission)

        # Commit the changes
        db.session.commit()

if __name__ == '__main__':
    seed_database()
