from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DB_engine.ModelOfData.Shipment_Table.shipment import Shipment, Base


class ShipmentDB:

    def __init__(self, ip_connect='', db_name=''):
        self.db_type = 'mysql'
        self.db_Shipment = 'root'
        self.db_consumer_id = ''
        self.ip_connect = '192.168.5.220'
        self.db_name = 'warehouse'
        self.engine = create_engine(
            f"{self.db_type}://{self.db_Shipment}:{self.db_consumer_id}@{self.ip_connect}/{self.db_name}")
        self.shipments = []
        self.shipment = {}
        Base.metadata.create_all(bind=self.engine)

    @property
    def last_id(self):
        e_s = self.readall()
        e_s_id = 0
        if len(e_s) > 0:
            e_s_id = e_s[len(e_s) - 1]['id']
        return e_s_id

    def add(self, index, date, user_id, consumer_id, weight):
        # создаем сессию подключения к бд
        with Session(autoflush=False, bind=self.engine) as db:
            # создаем объект Person для добавления в бд
            self.shipment = Shipment()
            self.shipment.id = index
            self.shipment.date = date
            self.shipment.User_id = user_id
            self.shipment.Consumer_id = consumer_id
            self.shipment.weight = weight

            db.add(self.shipment)  # добавляем в бд
            db.commit()  # сохраняем изменения
            # print(self.shipment.id)  # можно получить установленный id

    def readone(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.shipments = []
            self.shipment = db.query(Shipment).filter(index == Shipment.id)
            for shipment in self.shipment:
                self.shipments.append(
                    {
                        'id': shipment.id,
                        'date': shipment.date,
                        'user_id': shipment.user_id,
                        'Consumer_id': shipment.Consumer_id
                     }
                )  # f"{usr.id}, {usr.Name}, {usr.LastName}, {usr.LastEnter}, {usr.user_id}, {usr.Pass}, {usr.Role}"
        # print("Отработал sqlalchemy")
        return self.shipments

    def readall(self):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.shipments = []
            shipments = db.query(Shipment).all()
            for shipment in shipments:
                self.shipments.append(
                    {
                        'id': shipment.id,
                        'date': shipment.date,
                        'user_id': shipment.User_id,
                        'Consumer_id': shipment.Consumer_id,
                        'Weight':shipment.Weight
                    }
                )
        return self.shipments

    def update(self, index, date, user_id, consumer_id):
        with Session(autoflush=False, bind=self.engine) as db:
            self.shipment = db.query(Shipment).filter(index == Shipment.id).first()
            if None != self.shipment:
                # изменениям значения
                if date != '' and self.shipment.date != date:
                    self.shipment.id = date
                if user_id != '' and self.shipment.user_id != user_id:
                    self.shipment.user_id = user_id
                if consumer_id != '' and self.shipment.Consumer_id != consumer_id:
                    self.shipment.Consumer_id = consumer_id
                db.commit()  # сохраняем изменения
                self.shipment = db.query(Shipment).filter(Shipment.id == index).first()
                # print(f"{self.shipment.id}.{self.shipment.date} ({self.shipment.Consumer_id})")

    def delete(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            shipment = db.query(Shipment).filter(Shipment.id == index).first()
            db.delete(shipment)  # удаляем объект
            db.commit()  # сохраняем изменения
        return "Ok"
