
from DB_engine.ModelOfData.Based import Base
from sqlalchemy import Column, Integer, Date


class Shipment(Base):
    __tablename__ = "Shipment"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    User_id = Column(Integer)
    Consumer_id = Column(Integer)


# id Отгрузка - Отправка продукции потребителю
# Date
# User_id
# Consumer_id
