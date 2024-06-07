from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class ShipmentEvent(Base):
    __tablename__ = 'shipment_event'

    id = Column(Integer, primary_key=True)
    Event_Date = Column(DateTime)
    Comment = Column(String)
    User_id = Column(Integer)
    Shipment_id = Column(Integer)
    Status_id = Column(Integer)


class ShipmentEventTable:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def get_all(self):
        return self.session.query(ShipmentEvent).all()

    def get_by_id(self, shipment_event_id):
        return self.session.query(ShipmentEvent).filter_by(id=shipment_event_id).first()

    def create(self, event_date, comment, user_id, shipment_id, status_id):
        shipment_event = ShipmentEvent(Event_Date=event_date, Comment=comment, User_id=user_id, Shipment_id=shipment_id,
                                       Status_id=status_id)
        self.session.add(shipment_event)
        self.session.commit()

    def update(self, shipment_event_id, **kwargs):
        shipment_event = self.session.query(ShipmentEvent).filter_by(id=shipment_event_id).first()
        for key, value in kwargs.items():
            setattr(shipment_event, key, value)
        self.session.commit()

    def delete(self, shipment_event_id):
        shipment_event = self.session.query(ShipmentEvent).filter_by(id=shipment_event_id).first()
        self.session.delete(shipment_event)
        self.session.commit()
