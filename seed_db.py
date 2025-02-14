import pandas as pd
from app import create_app, db
from models import Passenger

app = create_app()
df = pd.read_csv("data/titanic.csv")

with app.app_context():
    db.create_all()  # Ensure tables exist

    for _, row in df.iterrows():
        passenger = Passenger(
            name=row['Name'],
            age=row['Age'] if pd.notna(row['Age']) else None,
            gender=row['Sex'],
            survived=row['Survived'],
            fare=row['Fare']
        )
        db.session.add(passenger)

    db.session.commit()
    print("Database seeded successfully!")
