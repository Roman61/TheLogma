
from DB_engine.ModelOfData.Based import Base
from sqlalchemy import Column, Integer, Date


class ShipmentEvent(Base):
    __tablename__ = "shipment_event"

    id = Column(Integer, primary_key=True, index=True)
    Shipment_id = Column(Integer)
    Status_id = Column(Integer)
    Event_Date = Column(Date)
    User_id = Column(Integer)


# id Событие по отгрузке продукта потребителю
# Shipment_id
# Status_id
# Event_Date
# User_id
