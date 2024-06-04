from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DB_engine.ModelOfData.Delivery_Table.delivery_event import DeliveryEvent, Base


class delivery_event_db:

    def __init__(self, ip_connect='', db_name=''):
        self.db_type = 'mysql'
        self.db_delivery_event = 'root'
        self.db_password = ''
        self.ip_connect = '192.168.5.220'
        self.db_name = 'warehouse'
        self.engine = create_engine(
            f"{self.db_type}://{self.db_delivery_event}:{self.db_password}@{self.ip_connect}/{self.db_name}")
        self.delivery_events = []
        self.delivery_event = {}
        Base.metadata.create_all(bind=self.engine)

    def add(self, index, name, Status_id, last_enter, User_id):
        # создаем сессию подключения к бд
        with Session(autoflush=False, bind=self.engine) as db:
            # создаем объект Person для добавления в бд
            self.delivery_event = DeliveryEvent(id=index, Name=name, Status_id=Status_id, Event_Date=last_enter,
                                                User_id=User_id)
            db.add(self.delivery_event)  # добавляем в бд
            db.commit()  # сохраняем изменения
            print(self.delivery_event.id)  # можно получить установленный id

    def readone(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.delivery_events = []
            self.delivery_event = db.query(DeliveryEvent).filter(index == DeliveryEvent.id)
            for dle in self.delivery_event:
                self.delivery_events.append({'id': dle.id, 'Delivery_id': dle.Delivery_id, 'Status_id': dle.Status_id,
                                             'Event_Date': dle.Event_Date,
                                             'User_id': dle.User_id})
        # print("Отработал sqlalchemy")
        return self.delivery_events

    @property
    def last_id(self):
        e_s = self.readall()
        e_s_id = 0
        if len(e_s) > 0:
            e_s_id = e_s[len(e_s) - 1]['id'] + 1
        return e_s_id

    def readall(self):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.delivery_events = []
            delivery_events = db.query(DeliveryEvent).all()
            for dle in delivery_events:
                self.delivery_events.append({'id': dle.id, 'Delivery_id': dle.Delivery_id, 'Status_id': dle.Status_id,
                                             'Event_Date': dle.Event_Date,
                                             'User_id': dle.User_id})
        return self.delivery_events

    def update(self, index, name='', Status_id='', last_enter='1970-01-01 00:00:00', user_id=''):
        with Session(autoflush=False, bind=self.engine) as db:
            self.delivery_event = db.query(DeliveryEvent).filter(index == DeliveryEvent.id).first()
            if None != self.delivery_event:
                # изменениям значения
                if name != '' and self.delivery_event.Name != name:
                    self.delivery_event.Name = name
                if Status_id != '' and self.delivery_event.Status_id != Status_id:
                    self.delivery_event.Status_id = Status_id
                if last_enter != '1970-01-01 00:00:00' and self.delivery_event.Event_Date != last_enter:
                    self.delivery_event.Event_Date = last_enter
                if user_id != '' and self.delivery_event.User_id != user_id:
                    self.delivery_event.User_id = user_id

                db.commit()  # сохраняем изменения

                self.delivery_event = db.query(DeliveryEvent).filter(DeliveryEvent.id == index).first()
                print(f"{self.delivery_event.id}.{self.delivery_event.Name} ({self.delivery_event.Status_id})")

    def delete(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            usr = db.query(DeliveryEvent).filter(DeliveryEvent.id == index).first()
            db.delete(usr)  # удаляем объект
            db.commit()  # сохраняем изменения
        return "Ok"
