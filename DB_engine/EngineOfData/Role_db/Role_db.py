from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from DB_engine.ModelOfData.Role_Table.Role import Role, Base


class RoleDB:

    def __init__(self):
        self.db_type = 'mysql'
        self.db_role = 'root'
        self.db_password = ''
        self.ip_connect = '192.168.5.220'
        self.db_name = 'warehouse'
        self.engine = create_engine(
            f"{self.db_type}://{self.db_role}:{self.db_password}@{self.ip_connect}/{self.db_name}")
        self.roles = []
        self.role = {}
        Base.metadata.create_all(bind=self.engine)

    @property
    def last_id(self):
        e_s = self.readall()
        e_s_id = 0
        if len(e_s) > 0:
            e_s_id = e_s[len(e_s) - 1]['id']
        return e_s_id

    # id = Column(Integer, primary_key=True, index=True)
    # Comment = Column(String)
    # Create = Column(Date)
    def add(self, index, comment, create):
        # создаем сессию подключения к бд
        with Session(autoflush=False, bind=self.engine) as db:
            # создаем объект Person для добавления в бд
            self.role = Role(id=index, Comment=comment, Create=create)
            db.add(self.role)  # добавляем в бд
            db.commit()  # сохраняем изменения
            # print(self.role.id)  # можно получить установленный id

    def readone(self, index):
        self.roles = []
        with Session(autoflush=False, bind=self.engine) as db:
            self.roles = db.query(Role).filter(index == Role.id)
            for role in self.roles:
                self.roles.append({'id': role.id, 'Comment': role.Comment, 'Create': role.Create})
         
        return self.roles

    def readall(self):
        self.roles = []
        with Session(autoflush=False, bind=self.engine) as db:
            # получение всех объектов
            roles_ = db.query(Role).all()
            for rol in roles_:
                self.roles.append({'id': rol.id, 'Comment': rol.Comment, 'Create': rol.Create})
        return self.roles

    # id Comment Create
    def update(self, index, comment='', create='1970-01-01 00:00:00'):
        with Session(autoflush=False, bind=self.engine) as db:
            self.role = db.query(Role).filter(index == Role.id).first()
            if self.role:

                # изменениям значения

                if comment != '' and self.role.Comment != comment:
                    self.role.Name = comment
                if create != '1970-01-01 00:00:00' and self.role.Create != create:
                    self.role.Create = create

                db.commit()  # сохраняем изменения

                self.role = db.query(Role).filter(Role.id == index).first()
                print(f"{self.role.id}.{self.role.Name} ({self.role.LastName})")

    def delete(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            role = db.query(Role).filter(Role.id == index).first()
            db.delete(role)  # удаляем объект
            db.commit()  # сохраняем изменения
        return "Ok"
