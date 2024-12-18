from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class DeliveryEvent(Base):
    __tablename__ = 'delivery_event'

    id = Column(Integer, primary_key=True)
    Event_Date = Column(DateTime)
    Comment = Column(String)
    User_id = Column(Integer)
    Delivery_id = Column(Integer)
    Status_id = Column(Integer)


class DeliveryEventTable:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def get_all(self):
        return self.session.query(DeliveryEvent).all()

    def get_by_id(self, event_id):
        return self.session.query(DeliveryEvent).filter_by(id=event_id).first()

    def create(self, event_date, comment, user_id, delivery_id, status_id):
        delivery_event = DeliveryEvent(Event_Date=event_date, Comment=comment, User_id=user_id, Delivery_id=delivery_id,
                                       Status_id=status_id)
        self.session.add(delivery_event)
        self.session.commit()

    def update(self, event_id, **kwargs):
        delivery_event = self.session.query(DeliveryEvent).filter_by(id=event_id).first()
        for key, value in kwargs.items():
            setattr(delivery_event, key, value)
        self.session.commit()

    def delete(self, event_id):
        delivery_event = self.session.query(DeliveryEvent).filter_by(id=event_id).first()
        self.session.delete(delivery_event)
        self.session.commit()
