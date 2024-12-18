from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True)
    Type = Column(String)
    Name = Column(String)
    User_id = Column(Integer)


class StatusTable:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def get_all(self):
        return self.session.query(Status).all()

    def get_by_id(self, status_id):
        return self.session.query(Status).filter_by(id=status_id).first()

    def create(self, type_, name, user_id):
        status = Status(Type=type_, Name=name, User_id=user_id)
        self.session.add(status)
        self.session.commit()

    def update(self, status_id, **kwargs):
        status = self.session.query(Status).filter_by(id=status_id).first()
        for key, value in kwargs.items():
            setattr(status, key, value)
        self.session.commit()

    def delete(self, status_id):
        status = self.session.query(Status).filter_by(id=status_id).first()
        self.session.delete(status)
        self.session.commit()
