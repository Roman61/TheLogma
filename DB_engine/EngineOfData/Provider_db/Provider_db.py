import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DB_engine.ModelOfData.Provider_Table.provider import Provider, Base


class ProviderDB:

    def __init__(self, ip_connect='', db_name=''):
        self.db_type = 'mysql'
        self.user_name = 'root'
        self.db_password = ''
        self.ip_connect = '192.168.5.220'
        self.db_name = 'warehouse'
        self.engine = create_engine(
            f"{self.db_type}://{self.user_name}:{self.db_password}@{self.ip_connect}/{self.db_name}")
        self.providers = []
        self.provider = {}
        Base.metadata.create_all(bind=self.engine)

    @property
    def last_id(self):
        e_s = self.readall()
        e_s_id = 0
        if len(e_s) > 0:
            e_s_id = e_s[len(e_s) - 1]['id']
        return e_s_id

    def add(self, index, name, lastname, registration):
        # создаем сессию подключения к бд
        with Session(autoflush=False, bind=self.engine) as db:
            # создаем объект Person для добавления в бд
            self.provider = Provider(id=index, Name=name, LastName=lastname, Registration=registration)
            db.add(self.provider)  # добавляем в бд
            db.commit()  # сохраняем изменения
            print(self.provider.id)  # можно получить установленный id

    def readone(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.providers = []
            self.provider = db.query(Provider).filter(index == Provider.id)
            for prv in self.provider:
                self.providers.append({'id': prv.id, 'Name': prv.Name, 'LastName': prv.LastName,
                                       'Registration': prv.Registration})
        # print("Отработал sqlalchemy")
        return self.providers

    def readall(self):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.providers = []
            providers = db.query(Provider).all()
            for prv in providers:
                self.providers.append(
                    {'id': prv.id, 'Name': prv.Name, 'LastName': prv.LastName, 'Registration': prv.Registration})
        return self.providers

    def update(self, index, name='', lastname='', registration='1970-01-01 00:00:00'):
        with Session(autoflush=False, bind=self.engine) as db:
            self.provider = db.query(Provider).filter(index == Provider.id).first()
            if None != self.provider:
                # изменениям значения
                if name != '' and self.provider.Name != name:
                    self.provider.Name = name
                if lastname != '' and self.provider.LastName != lastname:
                    self.provider.LastName = lastname
                if registration != '1970-01-01 00:00:00' and self.provider.LastEnter != registration:
                    self.provider.Registration = registration
                db.commit()  # сохраняем изменения
                self.provider = db.query(Provider).filter(Provider.id == index).first()
                print(f"{self.provider.id}.{self.provider.Name} ({self.provider.LastName})")

    def delete(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            usr = db.query(Provider).filter(Provider.id == index).first()
            db.delete(usr)  # удаляем объект
            db.commit()  # сохраняем изменения
        return "Ok"


