from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from User import Base, User


class UserEngine:

    def __init__(self, IP, db_name='warehouse'):#192.168.5.220/
        self.engine = create_engine("mysql://root:@"+IP+"/"+db_name+"")
        self.users = None
        self.user = None
        Base.metadata.create_all(bind=self.engine)

    def add(self, index, name, lastname, last_enter, logg_in, password, role):
        # создаем сессию подключения к бд
        with Session(autoflush=False, bind=self.engine) as db:
            # создаем объект Person для добавления в бд
            self.user = User(id=index, Name=name, LastName=lastname, LastEnter=last_enter, Loggin=logg_in, Pass=password,
                             Role=role)
            db.add(self.user)  # добавляем в бд
            db.commit()  # сохраняем изменения
            print(self.user.id)  # можно получить установленный id

    def readall(self):
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.users = db.query(User).all()
            for usr in self.users:
                print(f"{usr.id}, {usr.Name}, {usr.LastName}, {usr.LastEnter}, {usr.Loggin}, {usr.Pass}, {usr.Role}")
        print("Отработал sqlalchemy")
        return self.users

    def readone(self, index):
        user = None
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            self.user = db.query(User).filter(index == User.id)
            for usr in self.user:
                print(f"{usr.id}, {usr.Name}, {usr.LastName}, {usr.LastEnter}, {usr.Loggin}, {usr.Pass}, {usr.Role}")

        print("Отработал sqlalchemy")
        return self.user

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
