#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

class DBStorage:
    """Database storage class using SQLAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        self.__engine = create_engine('mysql+pymysql://{}:{}@{}:3306/{}'
                              .format(os.environ['HBNB_MYSQL_USER'],
                                      os.environ['HBNB_MYSQL_PWD'],
                                      os.environ['HBNB_MYSQL_HOST'],
                                      os.environ['HBNB_MYSQL_DB']),
                              pool_pre_ping=True)


        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session (self.__session)"""
        ...

    def new(self, obj):
        """Add the object to the current database session"""
        ...

    def save(self):
        """Commit all changes of the current database session"""
        ...

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        ...

    def reload(self):
        """Create all tables in the database and create the current database session"""
        ...
    
    def close(self):
        """Call remove() method on the private session attribute (self.__session)"""
        self.__session.remove()
        
# Create a DBStorage instance
storage = DBStorage()
storage.reload()
