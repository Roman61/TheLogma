from DB_engine.ModelOfData.Based import Base
from sqlalchemy import Column, Integer, String, Date


class User(Base):
    __tablename__ = "user"
# 	id	Name	LastName	LastEnter	Loggin	Pass	Role_User_id
    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    LastName = Column(String)
    LastEnter = Column(Date)
    Loggin = Column(String)
    Pass = Column(String)
    Role_User_id = Column(Integer, primary_key=True)
