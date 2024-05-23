from DB_engine.ModelOfData.Based import Base
from sqlalchemy import Column, Integer, String, Date


class AbstractData(Base):
    __tablename__ = "Abstract"

    id = Column(Integer, primary_key=True, index=True)

