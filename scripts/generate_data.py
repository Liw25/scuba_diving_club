import random
from faker import Faker
from datetime import datetime
from app.database import db_session
from app.models import Member, TrainingSession, Instructor, Guide, Tour

fake = Faker()

def create_members(n):
    for _ in range(n):
        member = Member(
            name=fake.name(),
            contact_info=fake.email(),
            certification_level=random.choice(['Beginner', 'Intermediate', 'Advanced']),
            date_joined=fake.past_date(start_date="-3y"),
            emergency_contact=fake.phone_number()
        )
        db_session.add(member)
    db_session.commit()

def create_instructors(n):
    for _ in range(n):
        instructor = Instructor(
            name=fake.name()
        )
        db_session.add(instructor)
    db_session.commit()

def create_guides(n):
    for _ in range(n):
        guide = Guide(
            name=fake.name()
        )
        db_session.add(guide)
    db_session.commit()

def create_training_sessions(n):
    instructors = db_session.query(Instructor).all()
    for _ in range(n):
        if instructors:
            session = TrainingSession(
                type=random.choice(['Pool', 'Open Water', 'Rescue']),
                date=fake.future_date(end_date="+30d"),
                time=f"{random.randint(8, 18)}:00",
                cost=random.uniform(50, 200),
                instructor=random.choice(instructors)
            )
            db_session.add(session)
    db_session.commit()

def create_tours(n):
    guides = db_session.query(Guide).all()
    for _ in range(n):
        if guides:
            tour = Tour(
                destination=fake.city(),
                start_date=fake.future_date(end_date="+1y"),
                end_date=fake.future_date(start_date="+1y", end_date="+2y"),
                guide=random.choice(guides),
                cost=random.uniform(100, 1000),
                max_participants=random.randint(5, 20)
            )
            db_session.add(tour)
    db_session.commit()

def main():
    create_members(50)
    create_instructors(10)
    create_guides(10)
    create_training_sessions(100)
    create_tours(30)

if __name__ == '__main__':
    main()
