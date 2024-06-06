import datetime
import time
from random import randint

from DB_engine.EngineOfData.Role_db.Role_db import RoleDB
from DB_engine.ModelOfData.Role_Table.Role import Role
from faker import Faker

# class TestUser:
#
# def __init__(self):
role_s = []


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
    e_role = RoleDB()
    assert e_role is not None


def test_add_delete_user():
    fake = Faker("ru_RU")

    e_role = RoleDB()
    rl_s = []
    j = last_id_to_rang_writing_test(e_role)    # id Comment Create
    for k in range(*j):
        role = Role()
        role.id = k
        role.Comment = fake.administrative_unit()
        role.Create = datetime.datetime.now()
        rl_s.append(role)
    len_db_2 = len(e_role.readall())
    for i in rl_s:
        e_role.add(index=i.id, comment=i.Comment, create=i.Create)
        role_s.append(i)

    len_self = len(role_s)
    len_execute_db = len(e_role.readall())
    result = len_execute_db - len_db_2 == len_self
    assert result

    len_self = len(role_s)
    len_db_2 = len(e_role.readall())

    for i in role_s:
        e_role.delete(index=i.id)
    len_execute_db = len(e_role.readall())
    assert len_execute_db == len_db_2 - len_self


def test_last_id():
    e_role = RoleDB()
    all_ = e_role.readall()
    assert e_role.last_id == all_[len(all_)-1]['id']


# def test_delete_user():
#     # = "mysql://root:@192.168.5.220/warehouse"
#     e_user = RoleDB()
#     len_db = len(e_user.readall())
#     e_user.delete(e_user.last_id)
#     len_execute_db = len(e_user.readall())
#     assert len_db - 1 == len_execute_db


# if __name__ == "__main__":
#     # test_user = TestUser()
#     print("1 --- test connect to db: " + test_connect_to_db())
#     print("2 --- test add delete user: " + test_add_delete_user())
