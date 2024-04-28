from flask import Flask, request, jsonify, abort
from models import Member, TrainingSession  # Ensure you have a session management in your database.py
from database import db_session

def register_routes(app):
    @app.route('/')
    def home():
        return "Welcome to the Scuba Diving Club!"

    # Member Routes
    @app.route('/members', methods=['GET'])
    def get_members():
        members = db_session.query(Member).all()
        return jsonify([member.to_dict() for member in members])

    @app.route('/members/<int:member_id>', methods=['GET'])
    def get_member(member_id):
        member = db_session.query(Member).filter(Member.id == member_id).first()
        if member:
            return jsonify(member.to_dict())
        abort(404, description="Member not found")

    @app.route('/members', methods=['POST'])
    def create_member():
        data = request.json
        new_member = Member(name=data['name'], contact_info=data['contact_info'])
        db_session.add(new_member)
        try:
            db_session.commit()
            return jsonify(new_member.to_dict()), 201
        except:
            db_session.rollback()
            abort(500)
        finally:
            db_session.remove()  # This ensures the session is properly closed after the request

    @app.route('/members/<int:member_id>', methods=['PUT'])
    def update_member(member_id):
        member = db_session.query(Member).filter(Member.id == member_id).first()
        if not member:
            abort(404, description="Member not found")

        data = request.get_json()
        member.name = data.get('name', member.name)
        member.contact_info = data.get('contact_info', member.contact_info)
        member.certification_level = data.get('certification_level', member.certification_level)
        member.emergency_contact = data.get('emergency_contact', member.emergency_contact)
        db_session.commit()
        return jsonify(member.to_dict())

    @app.route('/members/<int:member_id>', methods=['DELETE'])
    def delete_member(member_id):
        member = db_session.query(Member).filter(Member.id == member_id).first()
        if not member:
            abort(404, description="Member not found")

        db_session.delete(member)
        db_session.commit()
        return jsonify({'message': 'Member deleted successfully'})

    # Training Session Routes
    @app.route('/training_sessions', methods=['GET'])
    def get_training_sessions():
        sessions = db_session.query(TrainingSession).all()
        return jsonify([session.to_dict() for session in sessions])

    @app.route('/training_sessions/<int:session_id>', methods=['GET'])
    def get_training_session(session_id):
        session = db_session.query(TrainingSession).filter(TrainingSession.id == session_id).first()
        if session:
            return jsonify(session.to_dict())
        abort(404, description="Training session not found")

    # Additional routes for creating, updating, and deleting training sessions can be added similarly.

# Utility to convert model instances to dictionaries for JSON responses
def model_to_dict(model):
    return {column.name: getattr(model, column.name) for column in model.__table__.columns}

# Assuming each model class has this method for converting to dict
Member.to_dict = model_to_dict
TrainingSession.to_dict = model_to_dict
