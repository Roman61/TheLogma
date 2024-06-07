from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class Shipment(Base):
    __tablename__ = 'shipment'

    id = Column(Integer, primary_key=True)
    Date = Column(DateTime)
    Comment = Column(String)
    Consumer_id = Column(Integer)
    User_id = Column(Integer)


class ShipmentTable:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def get_all(self):
        return self.session.query(Shipment).all()

    def get_by_id(self, shipment_id):
        return self.session.query(Shipment).filter_by(id=shipment_id).first()

    def create(self, date, comment, consumer_id, user_id):
        shipment = Shipment(Date=date, Comment=comment, Consumer_id=consumer_id, User_id=user_id)
        self.session.add(shipment)
        self.session.commit()

    def update(self, shipment_id, **kwargs):
        shipment = self.session.query(Shipment).filter_by(id=shipment_id).first()
        for key, value in kwargs.items():
            setattr(shipment, key, value)
        self.session.commit()

    def delete(self, shipment_id):
        shipment = self.session.query(Shipment).filter_by(id=shipment_id).first()
        self.session.delete(shipment)
        self.session.commit()
