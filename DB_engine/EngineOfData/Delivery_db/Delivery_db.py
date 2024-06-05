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

    def add(self, index, date, user_id, provider_id):
        # создаем сессию подключения к бд
        with Session(autoflush=False, bind=self.engine) as db:
            # создаем объект Person для добавления в бд
            self.delivery = Delivery(id=index, Date=date, User_id=user_id, Provider_id=provider_id)
            db.add(self.delivery)  # добавляем в бд
            db.commit()  # сохраняем изменения
            print(self.delivery.id)  # можно получить установленный id

    def readone(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.deliverys = []
            self.delivery = db.query(Delivery).filter(index == Delivery.id)
            for dlv in self.delivery:
                self.deliverys.append({'id': dlv.id, 'Date': dlv.Date, 'User_id': dlv.User_id, 'Provider_id': dlv.Provider_id})
        # print("Отработал sqlalchemy")
        return self.deliverys

    @property
    def last_id(self):
        e_s = self.readall()
        e_s_id = 0
        if len(e_s) > 0:
            e_s_id = e_s[len(e_s) - 1]['id']
        return e_s_id

    def readall(self):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.deliverys = []
            deliverys = db.query(Delivery).all()
            for dlv in deliverys:
                self.deliverys.append({'id': dlv.id, 'Date': dlv.Date, 'User_id': dlv.User_id, 'Provider_id': dlv.Provider_id})
        return self.deliverys

    def update(self, index, user_id=0, date='1970-01-01 00:00:00', provider_id=0):
        with Session(autoflush=False, bind=self.engine) as db:
            self.delivery = db.query(Delivery).filter(index == Delivery.id).first()
            if None != self.delivery:

                # изменениям значения

                if user_id != '' and self.delivery.User_id != user_id:
                    self.delivery.User_id = user_id
                if date != '1970-01-01 00:00:00' and self.delivery.Date != date:
                    self.delivery.Date = date
                if provider_id != '' and self.delivery.Provider_id != provider_id:
                    self.delivery.Provider_id = provider_id

                db.commit()  # сохраняем изменения

                self.delivery = db.query(Delivery).filter(Delivery.id == index).first()
                print(f"{self.delivery.id}.{self.delivery.Date}.{self.delivery.User_id} ({self.delivery.Provider_id})")

    def delete(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            usr = db.query(Delivery).filter(Delivery.id == index).first()
            db.delete(usr)  # удаляем объект
            db.commit()  # сохраняем изменения
        return "Ok"
