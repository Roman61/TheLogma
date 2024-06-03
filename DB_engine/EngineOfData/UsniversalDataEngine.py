from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DB_engine.ModelOfData.Based import Base
from abc import ABC, abstractmethod


class UsniversalDataEngine:
    def __init__(self, db_type='mysql', db_user='root', db_password='', ip_connect='192.168.5.220', db_name='warehouse',
                 data_obj=None):
        self.db_type = db_type
        self.db_user = db_user
        self.db_password = db_password
        self.ip_connect = ip_connect
        self.db_name = db_name
        self.DataObj = data_obj
        self.engine = create_engine(
            f"{self.db_type}://{self.db_user}:{self.db_password}@{self.ip_connect}/{self.db_name}")
        Base.metadata.create_all(bind=self.engine)

    def add(self, index='', name='', lastname='', last_enter='', loggin='', password='', role='', data_obj=None):
        with Session(autoflush=False, bind=self.engine) as db:
            # создаем объект Person для добавления в бд
            self.DataObj = data_obj
            db.add(self.DataObj)  # добавляем в бд
            db.commit()  # сохраняем изменения
            print(self.DataObj.id)  # можно получить установленный id

    def readone(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов   # yes
            print(self.DataObj.__class__)
            # class_id = getattr(self.DataObj, 'id')
            # class_type =
            self.DataObj = db.query(self.DataObj.__class__).filter(self.DataObj.__class__.id==index)  # .filter(index == class_type.id)
            print(self.DataObj.__class__)
        return self.DataObj

    def readall(self):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.DataObj = db.query(self.DataObj.__class__).all()
        return self.DataObj

    def update(self, data_obj, index):
        def filter_attr(attr):
            if attr[:2] != '__' and attr[-2:] != '__':
                return True
            else:
                return False

        with Session(autoflush=False, bind=self.engine) as db:
            self.DataObj = db.query(self.DataObj.__class__).filter(index == getattr(self.DataObj, 'id')).first()
            if (None != self.DataObj) and (data_obj.__class__ == self.DataObj.__class__):
                attrs_self = list(filter(filter_attr, dir(self.DataObj)))
                for i in attrs_self:
                    if getattr(data_obj, i) != getattr(self.DataObj, i):
                        setattr(self.DataObj, i, getattr(data_obj, i))
                db.commit()  # сохраняем изменения
                self.DataObj = db.query(self.DataObj.__class__).filter(index == getattr(self.DataObj, 'id')).first()

    def delete(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            usr = db.query(self.DataObj.__class__).filter(self.DataObj.id == index).first()
            db.delete(usr)  # удаляем объект
            db.commit()  # сохраняем изменения
