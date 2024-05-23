from DB_engine.ModelOfData.Based import Base
from sqlalchemy import Column, Integer, Date


class DeliveryEvent(Base):
    __tablename__ = "delivery_event"

    id = Column(Integer, primary_key=True, index=True)
    Delivery_id = Column(Integer)
    Status_id = Column(Integer)
    Event_Date = Column(Date)
    User_id = Column(Integer)



# id Событие по доставке сырья на предприятие
# Delivery_id
# Status_id
# Event_Date
# User_id
