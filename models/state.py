from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class for storing state information"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    if models.storage_t != "db":
        @property
        def cities(self):
            """Getter method to return the list of City objects from storage linked to the current State"""
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]
