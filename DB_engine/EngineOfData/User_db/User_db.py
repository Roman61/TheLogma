from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DB_engine.ModelOfData.User_Table.User import User, Base


class UserDB:

    def __init__(self, ip_connect='', db_name=''):
        self.db_type = 'mysql'
        self.db_user = 'root'
        self.db_password = ''
        self.ip_connect = '192.168.5.220'
        self.db_name = 'warehouse'
        self.engine = create_engine(
            f"{self.db_type}://{self.db_user}:{self.db_password}@{self.ip_connect}/{self.db_name}")
        self.users = []
        self.user = {}
        Base.metadata.create_all(bind=self.engine)

    @property
    def last_id(self):
        e_s = self.readall()
        e_s_id = 0
        if len(e_s) > 0:
            e_s_id = e_s[len(e_s) - 1]['id']
        return e_s_id

    def add(self, index, name, lastname, last_enter, loggin, password, role):
        # создаем сессию подключения к бд
        with Session(autoflush=False, bind=self.engine) as db:
            # создаем объект Person для добавления в бд
            self.user = User(id=index, Name=name, LastName=lastname, LastEnter=last_enter, Loggin=loggin,
                             Pass=password, Role=role)
            db.add(self.user)  # добавляем в бд
            db.commit()  # сохраняем изменения
            # print(self.user.id)  # можно получить установленный id

    def readone(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.users = []
            self.user = db.query(User).filter(index == User.id)
            for usr in self.user:
                self.users.append({'id': usr.id, 'Name': usr.Name, 'LastName': usr.LastName, 'LastEnter': usr.LastEnter,
                                   'Loggin': usr.Loggin, 'Pass': usr.Pass,
                                   'Role': usr.Role})
        # print("Отработал sqlalchemy")
        return self.users

    def readall(self):
        self.users = []
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            users = db.query(User).all()
            for usr in users:
                self.users.append({'id': usr.id, 'Name': usr.Name, 'LastName': usr.LastName, 'LastEnter': usr.LastEnter,
                                   'Loggin': usr.Loggin, 'Pass': usr.Pass, 'Role': usr.Role})
        return self.users

    def update(self, index, name='', lastname='', last_enter='1970-01-01 00:00:00', logg_in='', password='', role=-1):
        with Session(autoflush=False, bind=self.engine) as db:
            self.user = db.query(User).filter(index == User.id).first()
            if None != self.user:

                # изменениям значения

                if name != '' and self.user.Name != name:
                    self.user.Name = name
                if lastname != '' and self.user.LastName != lastname:
                    self.user.LastName = lastname
                if last_enter != '1970-01-01 00:00:00' and self.user.LastEnter != last_enter:
                    self.user.LastEnter = last_enter
                if logg_in != '' and self.user.Loggin != logg_in:
                    self.user.Loggin = logg_in
                if password != '' and self.user.Pass != password:
                    self.user.Pass = password
                if role != -1 and self.user.Role != role:
                    self.user.Role = role

                db.commit()  # сохраняем изменения

                self.user = db.query(User).filter(User.id == index).first()
                print(f"{self.user.id}.{self.user.Name} ({self.user.LastName})")

    def delete(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            usr = db.query(User).filter(User.id == index).first()
            db.delete(usr)  # удаляем объект
            db.commit()  # сохраняем изменения
        return "Ok"
