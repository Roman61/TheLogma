from DB_engine.ModelOfData.Based import Base
from sqlalchemy import Column, Integer, String, Date


class Provider(Base):
    __tablename__ = "Provider_db"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    LastName = Column(String)
    Registration = Column(Date)

# id Поставщик
# Name
# LastName
# Registration
