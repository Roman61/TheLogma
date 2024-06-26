
from DB_engine.ModelOfData.Based import Base
from sqlalchemy import Column, Integer, Date, String


class Shipment(Base):
    __tablename__ = "Shipment"

    id = Column(Integer, primary_key=True, index=True)
    User_id = Column(Integer, primary_key=True)
    Consumer_id = Column(Integer, primary_key=True)
    date = Column(Date)
    Comment = Column(String)
    Weight = Column(Integer)


# id Отгрузка - Отправка продукции потребителю
# Date
# User_id
# Consumer_id
