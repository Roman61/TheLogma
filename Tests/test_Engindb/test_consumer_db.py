import datetime
import time
from random import randint
import MySQLdb
import sqlalchemy

from DB_engine.EngineOfData.User_db.User_db import UserDB
from DB_engine.ModelOfData.User_Table.User import User
from faker import Faker


class TestUser:

    def __init__(self):
        self.usrs = []

    @staticmethod
    def last_id_to_rang_writing_test(e_):
        e_s = e_.readall()
        e_s_id = 0
        if len(e_s) > 0:
            e_s_id = e_s[len(e_s) - 1]['id'] + 1
        rand_bgn = randint(e_s_id, e_s_id + 10)
        rand_end = randint(rand_bgn, rand_bgn + 50) + 1
        return rand_bgn, rand_end

    def test_connect_to_db(self):
        # = "mysql://root:@192.168.5.220/warehouse"
        euser = UserDB()
        assert euser is not None
        return 'Ok'

    def test_add_delete_user(self):
        fake = Faker("ru_RU")

        def helper_range(digital):
            yield from range(1, digital)

        # = "mysql://root:@192.168.5.220/warehouse"
        euser = UserDB()
        result = False
        usr_s = []
        j = self.last_id_to_rang_writing_test(euser)
        for k in range(*j):
            usr = User()
            usr.id = k  # randint(10, 20000)
            usr.Name = fake.first_name()
            usr.LastName = fake.last_name()
            usr.LastEnter = datetime.time
            usr.Loggin = fake.password(length=randint(10, 20))
            usr.Pass = fake.password(length=randint(10, 20))
            usr.Role = helper_range(randint(100, 2000))
            usr_s.append(usr)
        len_db_2 = len(euser.readall())
        for i in usr_s:
            euser.add(index=i.id, name=i.Name, lastname=i.LastName, last_enter=i.LastEnter, loggin=i.Loggin,
                      password=i.Pass, role=i.Role)
            self.usrs.append(i)

        len_self = len(self.usrs)
        len_execute_db = len(euser.readall())
        result = len_execute_db - len_db_2 == len_self
        assert result

        len_self = len(self.usrs)
        len_db_2 = len(euser.readall())

        for i in self.usrs:
            euser.delete(index=i.id)
        len_execute_db = len(euser.readall())
        assert len_execute_db == len_db_2 - len_self
        return 'Ok'

    def test_delete_user(self):
        # = "mysql://root:@192.168.5.220/warehouse"
        euser = UserDB()
        len_self = len(self.usrs)
        len_db = len(euser.readall())
        for i in self.usrs:
            euser.delete(i.id)
        len_execute_db = len(euser.readall())
        assert len_db + len_self == len_execute_db
        return 'Ok'


if __name__ == "__main__":
    test_user = TestUser()
    print("1 --- test connect to db: " + (test_user.test_connect_to_db()))
    print("2 --- test add delete user: " + (test_user.test_add_delete_user()))
