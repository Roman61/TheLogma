#  id Name
from DB_engine.ModelOfData.Based import Base
from sqlalchemy import Column, Integer, String, Date


# id	Type	Name	User_id
class Status(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, index=True)
    Type = Column(Integer)
    Name = Column(String)
    User_id = Column(Integer)
