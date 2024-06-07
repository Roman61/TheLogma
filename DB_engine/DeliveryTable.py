from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class Delivery(Base):
    __tablename__ = 'delivery'

    id = Column(Integer, primary_key=True)
    Date = Column(DateTime)
    Comment = Column(String)
    User_id = Column(Integer)
    Provider_id = Column(Integer)


class DeliveryTable:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def get_all_deliveries(self):
        return self.session.query(Delivery).all()

    def get_delivery_by_id(self, delivery_id):
        return self.session.query(Delivery).filter_by(id=delivery_id).first()

    def create_delivery(self, date, comment, user_id, provider_id):
        delivery = Delivery(Date=date, Comment=comment, User_id=user_id, Provider_id=provider_id)
        self.session.add(delivery)
        self.session.commit()

    def update_delivery(self, delivery_id, **kwargs):
        delivery = self.session.query(Delivery).filter_by(id=delivery_id).first()
        for key, value in kwargs.items():
            setattr(delivery, key, value)
        self.session.commit()

    def delete_delivery(self, delivery_id):
        delivery = self.session.query(Delivery).filter_by(id=delivery_id).first()
        self.session.delete(delivery)
        self.session.commit()
