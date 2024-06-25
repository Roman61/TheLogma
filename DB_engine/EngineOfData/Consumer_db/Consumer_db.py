from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DB_engine.ModelOfData.Consumer_Table.consumer import Consumer, Base


class ConsumerDB:

    def __init__(self, ip_connect='', db_name=''):
        self.db_type = 'mysql'
        self.user_name = 'root'
        self.db_password = ''
        self.ip_connect = '192.168.5.220'
        self.db_name = 'warehouse'
        self.engine = create_engine(
            f"{self.db_type}://{self.user_name}:{self.db_password}@{self.ip_connect}/{self.db_name}")
        self.Consumers = []
        self.Consumer = {}
        Base.metadata.create_all(bind=self.engine)

    def add(self, index, name, lastname, registration):
        # создаем сессию подключения к бд
        with Session(autoflush=False, bind=self.engine) as db:
            # создаем объект Person для добавления в бд
            self.Consumer = Consumer(id=index, Name=name, LastName=lastname, Registration=registration)
            db.add(self.Consumer)  # добавляем в бд
            db.commit()  # сохраняем изменения
            #  print(self.Consumer.id)  # можно получить установленный id

    @property
    def last_id(self):
        e_s = self.readall()
        e_s_id = 0
        if len(e_s) > 0:
            e_s_id = e_s[len(e_s) - 1]['id']
        return e_s_id

    def readone(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.Consumers = []
            self.Consumer = db.query(Consumer).filter(index == Consumer.id)
            for cnsm in self.Consumer:
                self.Consumers.append(
                    {'id': cnsm.id, 'Name': cnsm.Name, 'LastName': cnsm.LastName, 'Registration': cnsm.Registration,
                     "fk_user_id": cnsm.fk_user_id})
        return self.Consumers

    def readall(self):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.Consumers = []
            consumers = db.query(Consumer).all()
            for cnsm in consumers:
                self.Consumers.append(
                    {'id': cnsm.id, 'Name': cnsm.Name, 'LastName': cnsm.LastName, 'Registration': cnsm.Registration,
                     "fk_user_id": cnsm.fk_user_id})
        return self.Consumers

    def update(self, index, name='', lastname='', registration='1970-01-01 00:00:00', logg_in='', password='', role=-1):
        with Session(autoflush=False, bind=self.engine) as db:
            self.Consumer = db.query(Consumer).filter(index == Consumer.id).first()
            if None != self.Consumer:

                # изменениям значения

                if name != '' and self.Consumer.Name != name:
                    self.Consumer.Name = name
                if lastname != '' and self.Consumer.LastName != lastname:
                    self.Consumer.LastName = lastname
                if registration != '1970-01-01 00:00:00' and self.Consumer.Registration != registration:
                    self.Consumer.Registration = registration

                db.commit()  # сохраняем изменения

                self.Consumer = db.query(Consumer).filter(Consumer.id == index).first()
                print(f"{self.Consumer.id}.{self.Consumer.Name} ({self.Consumer.LastName})")

    def delete(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            cnsm = db.query(Consumer).filter(Consumer.id == index).first()
            db.delete(cnsm)  # удаляем объект
            db.commit()  # сохраняем изменения
        return "Ok"


if __name__ == '__main__':
    provider_db = ConsumerDB()
    provider_db.add(
        index=2,
        name='Роман',
        lastname='Александрович',
        registration=datetime.now()
    )
