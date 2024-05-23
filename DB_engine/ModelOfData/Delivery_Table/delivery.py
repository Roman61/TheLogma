from DB_engine.ModelOfData.Based import Base
from sqlalchemy import Column, Integer, String, Date


class Delivery(Base):
    __tablename__ = "delivery"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    LastName = Column(String)
    Registration = Column(Date)



# id Потребитель
# Name
# LastName
# Registration
