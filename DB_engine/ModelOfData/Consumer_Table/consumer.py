from sqlalchemy import Column, Integer, String, Date
from DB_engine.ModelOfData.Based import Base


class Consumer(Base):
    __tablename__ = "consumer"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    LastName = Column(String)
    Registration = Column(Date)
    fk_user_id = Column(Integer, primary_key=True)

# id Потребитель
# Name
# LastName
# Registration
