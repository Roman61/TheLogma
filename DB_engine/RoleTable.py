from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    Comment = Column(String)
    Create = Column(DateTime)


class RoleTable:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def get_all(self):
        return self.session.query(Role).all()

    def get_by_id(self, role_id):
        return self.session.query(Role).filter_by(id=role_id).first()

    def create(self, comment, create_date):
        role = Role(Comment=comment, Create=create_date)
        self.session.add(role)
        self.session.commit()

    def update(self, role_id, **kwargs):
        role = self.session.query(Role).filter_by(id=role_id).first()
        for key, value in kwargs.items():
            setattr(role, key, value)
        self.session.commit()

    def delete(self, role_id):
        role = self.session.query(Role).filter_by(id=role_id).first()
        self.session.delete(role)
        self.session.commit()
