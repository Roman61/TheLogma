from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    Name = Column(String)
    LastName = Column(String)
    LastEnter = Column(DateTime)
    Loggin = Column(String)
    Pass = Column(String)
    Role_User_id = Column(Integer)
    IP = Column(String)


class UserTable:
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def get_all(self):
        return self.session.query(User).all()

    def get_by_id(self, user_id):
        return self.session.query(User).filter_by(id=user_id).first()

    def get_by_login(self, login):
        return self.session.query(User).filter_by(Loggin=login).first()

    def create(self, name, lastname, last_enter, login, password, role_user_id):
        user = User(Name=name, LastName=lastname, LastEnter=last_enter, Loggin=login, Pass=password,
                    Role_User_id=role_user_id)
        self.session.add(user)
        self.session.commit()

    def update(self, user_id, **kwargs):
        user = self.session.query(User).filter_by(id=user_id).first()
        for key, value in kwargs.items():
            setattr(user, key, value)
        self.session.commit()

    def delete(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        self.session.delete(user)
        self.session.commit()
