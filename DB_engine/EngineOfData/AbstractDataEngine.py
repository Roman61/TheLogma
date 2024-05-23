from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DB_engine.ModelOfData.Based import Base


class AbstractDataEngine:
    def __init__(self, connect_str, data_obj):
        self.engine = create_engine(connect_str)
        Base.metadata.create_all(bind=self.engine)
        self.DataObj = data_obj

    def add(self, data_obj):
        with Session(autoflush=False, bind=self.engine) as db:
            # создаем объект Person для добавления в бд
            self.DataObj = data_obj
            db.add(self.DataObj)  # добавляем в бд
            db.commit()  # сохраняем изменения
            print(self.DataObj.id)  # можно получить установленный id

    def readone(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов   # yes
            print(type(self.DataObj))
            self.DataObj = db.query(type(self.DataObj)).filter(index == getattr(self.DataObj, 'id'))
            print(type(self.DataObj))
        return self.DataObj

    def readall(self):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.DataObj = db.query(type(self.DataObj)).all()
        return self.DataObj

    def update(self, data_obj, index):
        def filter_attr(attr):
            if attr[:3] != '__' and attr[-2:] != '__':
                return True
            else:
                return False

        with Session(autoflush=False, bind=self.engine) as db:
            self.DataObj = db.query(type(self.DataObj)).filter(index == getattr(self.DataObj, 'id')).first()
            if (None != self.DataObj) and (type(data_obj) == type(self.DataObj)):
                attrs_self = list(filter(filter_attr, dir(self.DataObj)))
                for i in attrs_self:
                    if getattr(data_obj, i) != getattr(self.DataObj, i):
                        setattr(self.DataObj, i, getattr(data_obj, i))
                db.commit()  # сохраняем изменения
                self.DataObj = db.query(type(self.DataObj)).filter(index == getattr(self.DataObj, 'id')).first()

    def delete(self):
        pass
