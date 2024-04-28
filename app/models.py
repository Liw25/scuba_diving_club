from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from database import Base


class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    certification_level = Column(String)
    date_joined = Column(Date)
    emergency_contact = Column(String)

    # Relationships
    trainings = relationship("TrainingSession", back_populates="members")
    tours = relationship("Tour", secondary="member_tour_link")


class TrainingSession(Base):
    __tablename__ = 'training_sessions'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    date = Column(Date)
    time = Column(String)
    cost = Column(Float)
    instructor_id = Column(Integer, ForeignKey('instructors.id'))

    # Relationships
    members = relationship("Member", back_populates="trainings")
    instructor = relationship("Instructor", back_populates="trainings")


class Instructor(Base):
    __tablename__ = 'instructors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # Relationships
    trainings = relationship("TrainingSession", back_populates="instructor")


class Tour(Base):
    __tablename__ = 'tours'

    id = Column(Integer, primary_key=True, index=True)
    destination = Column(String, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    guide_id = Column(Integer, ForeignKey('guides.id'))
    cost = Column(Float)
    max_participants = Column(Integer)

    # Relationships
    members = relationship("Member", secondary="member_tour_link")
    guide = relationship("Guide", back_populates="tours")


class Guide(Base):
    __tablename__ = 'guides'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    # Relationships
    tours = relationship("Tour", back_populates="guide")


class MemberTourLink(Base):
    __tablename__ = 'member_tour_link'
    member_id = Column(Integer, ForeignKey('members.id'), primary_key=True)
    tour_id = Column(Integer, ForeignKey('tours.id'), primary_key=True)
