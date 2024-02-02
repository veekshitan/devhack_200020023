from core.settings import POSTGRES_USER, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_PASSWORD, POSTGRES_DBNAME
from core.postgres_connection import DatabaseManager, user_table, events_table, copouns, buy_copouns
from sqlalchemy import func,text, desc,cast, String, Date,and_
import json

db_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DBNAME}"
db_manager = DatabaseManager(db_url)
db_manager.create_tables()
session = db_manager.get_session()

def find_user(roll_number, password):
    return session.query(user_table).filter_by(and_(roll_number=roll_number, password=password)).first()

def get_user_by_roll_number(roll_number):
    user = (session.query(user_table).filter_by(and_(roll_number=roll_number)).first())
    if user:
        # Unpack the result tuple and return as a dictionary
        return {'name': user.name, 'email': user.email_id, 'contact_number': user.contact_no, 'roll_no': user.roll_no}
    else:
        return None

def add_event(roll_number,name, description,website_link,sub_events):
    return session.add(events_table(roll_number,name,description,website_link,sub_events))