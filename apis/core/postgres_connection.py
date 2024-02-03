from sqlalchemy import create_engine, Column, String, String, MetaData, JSON, Boolean,PrimaryKeyConstraint,Integer
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.dialects.postgresql import JSONB
import json


Base = declarative_base()

class user_table(Base):
    __tablename__ = 'user_table'
    user_id = Column(String, primary_key=True)
    name = Column(String)
    contact_no = Column(String)
    email_id = Column(String)
    roll_no = Column(String)
    can_add_event = Column(Boolean)
    can_add_coupons = Column(Boolean)
    password = Column(String)
    

class events_table(Base):
    __tablename__ = 'events_table'
    roll_no = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)
    website_link = Column(String)
    sub_events = Column(JSON)
    
class copouns(Base):
    __tablename__ = 'copouns'
    roll_no = Column(String)
    category = Column(String)
    __table_args__ = (
            PrimaryKeyConstraint('roll_no',  'category', name='_topic_table_level_uc'),
        )

class buy_copouns(Base):
    __tablename__ = 'buy_copouns'
    roll_no = Column(String)
    category = Column(String)
    __table_args__ = (
            PrimaryKeyConstraint('roll_no',  'category', name='_topic_table_level_uc1'),
        )

class items(Base):
    __tablename__ = 'items'
    roll_no = Column(String)
    category = Column(String)
    item_name = Column(String)
    cost = Column(String)
    images = Column(String)
    unique_good_number = Column(Integer, primary_key = True,autoincrement=True)
    
class DatabaseManager:
    _instance = None

    def __new__(cls, db_url):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db_url = db_url
            cls._instance.engine = create_engine(db_url)
            cls._instance.Session = sessionmaker(bind=cls._instance.engine)
            cls._instance.session = cls._instance.Session()
            cls._instance.metadata = MetaData()
            cls._instance.create_database()
        return cls._instance
    
    def create_database(self):
        if not database_exists(self.db_url):
            create_database(self.db_url)

    def create_tables(self):
        Base.metadata.create_all(self.engine, checkfirst=True)

    def get_session(self):
        return self.session