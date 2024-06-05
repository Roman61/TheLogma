from DB_engine.ModelOfData.Based import Base
from sqlalchemy import Column, Integer, String, Date


class Provider(Base):
    __tablename__ = "Provider"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String(45))
    LastName = Column(String(45))
    Registration = Column(Date)

# id Поставщик
# Name
# LastName
# Registration
