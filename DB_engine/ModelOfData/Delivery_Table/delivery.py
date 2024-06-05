from DB_engine.ModelOfData.Based import Base
from sqlalchemy import Column, Integer, String, Date


class Delivery(Base):
    __tablename__ = "delivery"

    id = Column(Integer, primary_key=True, index=True)
    Date = Column(Date)
    User_id = Column(Integer)
    Provider_id = Column(Integer)



# id Потребитель
# Name
# LastName
# Registration
