from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class Consumer(Base):
    __tablename__ = 'consumer'

    id = Column(Integer, primary_key=True)
    Name = Column(String)
    LastName = Column(String)
    Registration = Column(DateTime)
    User_id = Column(Integer)


class ConsumerTable:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def get_all(self):
        return self.session.query(Consumer).all()

    def get_by_id(self, id):
        return self.session.query(Consumer).filter_by(id=id).first()

    def create(self, name, last_name, registration, user_id):
        consumer = Consumer(Name=name, LastName=last_name, Registration=registration, User_id=user_id)
        self.session.add(consumer)
        self.session.commit()

    def update(self, id, **kwargs):
        consumer = self.session.query(Consumer).filter_by(id=id).first()
        for key, value in kwargs.items():
            setattr(consumer, key, value)
        self.session.commit()

    def delete(self, id):
        consumer = self.session.query(Consumer).filter_by(id=id).first()
        self.session.delete(consumer)
        self.session.commit()
