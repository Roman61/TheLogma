from datetime import datetime
import time
from random import randint
import MySQLdb
import sqlalchemy

from DB_engine.EngineOfData.Status_db.Status_db import Status
from DB_engine.ModelOfData.Status_Table.Status import Status
from DB_engine.ModelOfData.User_Table.User import User
from DB_engine.EngineOfData.User_db.User_db import UserDB
from faker import Faker

usrs = []


@staticmethod
def last_id_to_rang_writing_test(e_):
    e_s = e_.readall()
    e_s_id = 0
    if len(e_s) > 0:
        e_s_id = e_s[len(e_s) - 1]['id'] + 1
    rand_bgn = randint(e_s_id, e_s_id + 10)
    rand_end = randint(rand_bgn, rand_bgn + 50) + 1
    return rand_bgn, rand_end


def test_connect_to_db():
    euser = UserDB()
    assert euser is not None


def test_add_delete_user():
    fake = Faker("ru_RU")
    roles = RoleDB().readall()
    len_roles = len(roles) - 1
    euser = UserDB()
    usr_s = []
    j = last_id_to_rang_writing_test(euser)
    for k in range(*j):
        usr = User()
        usr.id = k
        usr.Name = fake.first_name()
        usr.LastName = fake.last_name()
        usr.LastEnter = datetime.now()
        usr.Loggin = fake.password(length=randint(10, 20))
        usr.Pass = fake.password(length=randint(10, 20))
        usr.Role_User_id = roles[randint(0, len_roles)]['id']
        usr_s.append(usr)
    len_db_2 = len(euser.readall())
    for i in usr_s:
        euser.add(index=i.id, name=i.Name, lastname=i.LastName, last_enter=i.LastEnter, loggin=i.Loggin,
                  password=i.Pass, role=i.Role_User_id)
        usrs.append(i)

    len_self = len(usrs)
    len_execute_db = len(euser.readall())
    result = len_execute_db - len_db_2 == len_self
    assert result

    len_self = len(usrs)
    len_db_2 = len(euser.readall())

    for i in usrs:
        euser.delete(index=i.id)
    len_execute_db = len(euser.readall())
    assert len_execute_db == len_db_2 - len_self


def test_last_id():
    euser = UserDB()
    all_ = euser.readall()
    assert euser.last_id == all_[len(all_)-1]['id']


# def test_delete_user():
#     # = "mysql://root:@192.168.5.220/warehouse"
#     e_user = UserDB()
#     len_db = len(e_user.readall())
#     e_user.delete(e_user.last_id)
#     len_execute_db = len(e_user.readall())
#     assert len_db - 1 == len_execute_db


# if __name__ == "__main__":
#     # test_user = TestUser()
#     print("1 --- test connect to db: " + test_connect_to_db())
#     print("2 --- test add delete user: " + test_add_delete_user())
