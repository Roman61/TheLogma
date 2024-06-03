from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DB_engine.ModelOfData.Delivery_Table.delivery import Delivery, Base


class DeliveryDB:

    def __init__(self, ip_connect='', db_name=''):
        self.db_type = 'mysql'
        self.db_Delivery = 'root'
        self.db_password = ''
        self.ip_connect = '192.168.5.220'
        self.db_name = 'warehouse'
        self.engine = create_engine(
            f"{self.db_type}://{self.db_Delivery}:{self.db_password}@{self.ip_connect}/{self.db_name}")
        self.deliverys = []
        self.delivery = {}
        Base.metadata.create_all(bind=self.engine)

    def add(self, index, name, lastname, last_enter, loggin, password, role):
        # создаем сессию подключения к бд
        with Session(autoflush=False, bind=self.engine) as db:
            # создаем объект Person для добавления в бд
            self.delivery = Delivery(id=index, Name=name, LastName=lastname, LastEnter=last_enter, Loggin=loggin,
                                     Pass=password, Role=role)
            db.add(self.delivery)  # добавляем в бд
            db.commit()  # сохраняем изменения
            print(self.delivery.id)  # можно получить установленный id

    def readone(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.deliverys = []
            self.delivery = db.query(Delivery).filter(index == Delivery.id)
            for dlv in self.delivery:
                self.deliverys.append({'id': dlv.id, 'Name': dlv.Name, 'LastName': dlv.LastName, 'Registration': dlv.Registration})
        # print("Отработал sqlalchemy")
        return self.deliverys

    def readall(self):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.deliverys = []
            deliverys = db.query(Delivery).all()
            for dlv in deliverys:
                self.deliverys.append({'id': dlv.id, 'Name': dlv.Name, 'LastName': dlv.LastName, 'Registration': dlv.Registration})
        return self.deliverys

    def update(self, index, name='', lastname='', last_enter='1970-01-01 00:00:00', logg_in='', password='', role=-1):
        with Session(autoflush=False, bind=self.engine) as db:
            self.delivery = db.query(Delivery).filter(index == Delivery.id).first()
            if None != self.delivery:

                # изменениям значения

                if name != '' and self.delivery.Name != name:
                    self.delivery.Name = name
                if lastname != '' and self.delivery.LastName != lastname:
                    self.delivery.LastName = lastname
                if last_enter != '1970-01-01 00:00:00' and self.delivery.LastEnter != last_enter:
                    self.delivery.LastEnter = last_enter
                if logg_in != '' and self.delivery.Loggin != logg_in:
                    self.delivery.Loggin = logg_in
                if password != '' and self.delivery.Pass != password:
                    self.delivery.Pass = password
                if role != -1 and self.delivery.Role != role:
                    self.delivery.Role = role

                db.commit()  # сохраняем изменения

                self.delivery = db.query(Delivery).filter(Delivery.id == index).first()
                print(f"{self.delivery.id}.{self.delivery.Name} ({self.delivery.LastName})")

    def delete(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            usr = db.query(Delivery).filter(Delivery.id == index).first()
            db.delete(usr)  # удаляем объект
            db.commit()  # сохраняем изменения
        return "Ok"
