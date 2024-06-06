# id	Comment	Create
from DB_engine.ModelOfData.Based import Base
from sqlalchemy import Column, Integer, String, Date


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    Comment = Column(String)
    Create = Column(Date)
