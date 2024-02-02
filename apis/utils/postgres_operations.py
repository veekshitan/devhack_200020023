from core.settings import POSTGRES_USER, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_PASSWORD, POSTGRES_DBNAME
from core.postgres_connection import DatabaseManager, user_table, events_table, copouns, buy_copouns,items
from sqlalchemy import func,text, desc,cast, String, Date,and_
import json

db_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DBNAME}"
db_manager = DatabaseManager(db_url)
db_manager.create_tables()
session = db_manager.get_session()

def find_user(roll_number, password):
    return session.query(user_table).filter_by(and_(roll_no=roll_number, password=password)).first()

def get_user_by_roll_number(roll_number):
    user = (session.query(user_table).filter_by(and_(roll_no=roll_number)).first())
    if user:
        return {'name': user.name, 'email': user.email_id, 'contact_number': user.contact_no, 'roll_no': user.roll_no}
    else:
        return None

def add_event(roll_number,name, description,website_link,sub_events):
    return session.add(events_table(roll_no=roll_number,name=name,description=description,website_link=website_link,sub_events=sub_events))

def get_all_events():
    return session.query(events_table).all()

def get_events_by_event_name(event_name):
    return session.query(events_table).filter_by(event_name=event_name).all()

def add_coupon(roll_no,category):
    return session.add(copouns(roll_no=roll_no,category=category))

def add_buy_coupon(roll_no,category):
    return session.add(buy_copouns(roll_no=roll_no,category=category))

def getSellerEmailID(good_number):
    item_details = session.query(items).filter_by(unique_good_number=good_number).first()

    if item_details:
        # Get the roll number from item_details
        roll_number = item_details.roll_no

        # Query the user_table to get the seller's details
        seller_details = session.query(user_table).filter_by(roll_no=roll_number).first()

        if seller_details:
            # Return item name, seller's email id, and seller's name
            return item_details.item_name, seller_details.email, seller_details.name
        else:
            print(f"Seller not found for roll number: {roll_number}")
            return None
    else:
        print(f"Item not found for good number: {good_number}")
        return None
  