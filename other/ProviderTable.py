from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class Provider(Base):
    __tablename__ = 'provider'

    id = Column(Integer, primary_key=True)
    Name = Column(String)
    LastName = Column(String)
    Registration = Column(DateTime)
    User_id = Column(Integer)


class ProviderTable:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def get_all(self):
        return self.session.query(Provider).all()

    def get_by_id(self, provider_id):
        return self.session.query(Provider).filter_by(id=provider_id).first()

    def create(self, name, last_name, registration, user_id):
        provider = Provider(Name=name, LastName=last_name, Registration=registration, User_id=user_id)
        self.session.add(provider)
        self.session.commit()

    def update(self, provider_id, **kwargs):
        provider = self.session.query(Provider).filter_by(id=provider_id).first()
        for key, value in kwargs.items():
            setattr(provider, key, value)
        self.session.commit()

    def delete(self, provider_id):
        provider = self.session.query(Provider).filter_by(id=provider_id).first()
        self.session.delete(provider)
        self.session.commit()
