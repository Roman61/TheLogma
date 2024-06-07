from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from DB_engine.ModelOfData.Status_Table.Status import Status, Base
import sqlalchemy.engine.reflection


class StatusDB:

    def __init__(self):
        self.db_type = 'mysql'
        self.db_role = 'root'
        self.db_password = ''
        self.ip_connect = '192.168.5.220'
        self.db_name = 'warehouse'
        self.engine = create_engine(
            f"{self.db_type}://{self.db_role}:{self.db_password}@{self.ip_connect}/{self.db_name}")
        self.statuses = []
        self.status = {}
        Base.metadata.create_all(bind=self.engine)

    def get_table_and_column_names(self):
        """
        Функция, которая получает объект engine SQLAlchemy и возвращает словарь,
        где ключами являются имена таблиц, а значениями - списки имен полей для каждой таблицы.
        """
        inspector = inspect(self.engine)
        table_and_column_names = {}

        for table_name in inspector.get_table_names():
            columns = inspector.get_columns(table_name)
            column_names = [column['name'] for column in columns]
            table_and_column_names[table_name] = column_names

        return table_and_column_names

    @property
    def last_id(self):
        e_s = self.readall()
        e_s_id = 0
        if len(e_s) > 0:
            e_s_id = e_s[len(e_s) - 1]['id']
        return e_s_id

    # Type Name User_id
    def add(self, index, type_, user_id, name):
        # создаем сессию подключения к бд
        with Session(autoflush=False, bind=self.engine) as db:
            # создаем объект Person для добавления в бд
            self.role = Status(id=index, Type=type_, User_id=user_id, Name=name)
            db.add(self.role)  # добавляем в бд
            db.commit()  # сохраняем изменения
            # print(self.role.id)  # можно получить установленный id

    # Type Name User_id
    def readone(self, index):
        statuses = []
        with Session(autoflush=False, bind=self.engine) as db:
            statuses = db.query(Status).filter(index == Status.id)
            for status in statuses:
                self.statuses.append(
                    {'id': status.id, 'Type': status.Type, 'Name': status.Name, 'User_id': status.User_id})

        return self.statuses

    # Type Name User_id
    def readall(self):

        statuses = []
        with Session(autoflush=False, bind=self.engine) as db:
            # table_names = db.

            # .Inspector.get_table_names()
            # получение всех объектов
            statuses = db.query(Status).all()
            for status in statuses:  # Type Name User_id
                self.statuses.append(
                    {'id': status.id, 'Type': status.Type, 'Name': status.Name, 'User_id': status.User_id})
        return self.statuses

    # Type Name User_id
    def update(self, index, type_='', name='1970-01-01 00:00:00', user_id=''):
        with Session(autoflush=False, bind=self.engine) as db:
            status = db.query(Status).filter(index == Status.id).first()
            if status:

                # изменениям значения
                if user_id != '' and status.User_id != user_id:
                    status.User_id = user_id
                if type_ != '' and status.Comment != type_:
                    status.Name = type_
                if name != '1970-01-01 00:00:00' and status.Name != name:
                    status.Name = name

                db.commit()  # сохраняем изменения

                status = db.query(Status).filter(Status.id == index).first()
                print(f"{status.id}.{status.Name} ({status.User_id})")

    def delete(self, index):
        with Session(autoflush=False, bind=self.engine) as db:
            role = db.query(Status).filter(Status.id == index).first()
            db.delete(role)  # удаляем объект
            db.commit()  # сохраняем изменения
        return "Ok"


if __name__ == "__main__":
    status = StatusDB()
    for table_name, column_names in status.get_table_and_column_names().items():
        print(f"Table: '{table_name}' columns: {', '.join(column_names)}")
