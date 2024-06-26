#  id Name
from DB_engine.ModelOfData.Based import Base
from sqlalchemy import Column, Integer, String, Date


# id	Type	Name	User_id
class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True, index=True)
    User_id = Column(Integer, primary_key=True)
    Type = Column(Integer)
    Name = Column(String)

