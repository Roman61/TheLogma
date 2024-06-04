import datetime
import time
from random import randint
import MySQLdb
import pytest
import sqlalchemy

from DB_engine.EngineOfData.Consumer_db.Consumer_db import ConsumerDB
from DB_engine.ModelOfData.Consumer_Table.consumer import Consumer
from faker import Faker

cnsmrs = []


def last_id_to_rang_writing_test(e_):
    e_s = e_.readall()
    e_s_id = 0
    if len(e_s) > 0:
        e_s_id = e_s[len(e_s) - 1]['id'] + 1
    rand_bgn = randint(e_s_id, e_s_id + 10)
    rand_end = randint(rand_bgn, rand_bgn + 50) + 1
    return rand_bgn, rand_end


def test_connect_to_db():
    ecnsmr = ConsumerDB()
    assert ecnsmr is not None


def test_last_id():
    euser = ConsumerDB()
    all_ = euser.readall()
    assert euser.last_id == all_[len(all_) - 1]['id']


def test_add_delete_consumer():
    fake = Faker("ru_RU")

    def helper_range(digital):
        yield from range(1, digital)

    e_consumer = ConsumerDB()
    cnsmr_s = []
    j = last_id_to_rang_writing_test(e_consumer)
    for k in range(*j):
        cnsmr = Consumer()
        cnsmr.id = k  # randint(10, 20000)
        cnsmr.Name = fake.first_name()
        cnsmr.LastName = fake.last_name()
        cnsmr.Registration = datetime.time
        cnsmr_s.append(cnsmr)
    len_db_2 = len(e_consumer.readall())
    for i in cnsmr_s:
        e_consumer.add(index=i.id, name=i.Name, lastname=i.LastName, registration=i.Registration)
        cnsmrs.append(i)

    len_self = len(cnsmrs)
    len_execute_db = len(e_consumer.readall())
    result = len_execute_db - len_db_2 == len_self
    assert result

    len_self = len(cnsmrs)
    len_db_2 = len(e_consumer.readall())

    for i in cnsmrs:
        e_consumer.delete(index=i.id)
    len_execute_db = len(e_consumer.readall())
    assert len_execute_db == len_db_2 - len_self


# def test_delete_consumer():
#     e_consumer = ConsumerDB()
#     len_db = len(e_consumer.readall())
#     e_consumer.delete(e_consumer.last_id)
#     len_execute_db = len(e_consumer.readall())
#     assert len_db - 1 == len_execute_db


# if __name__ == "__main__":
#     # test_consumer = Testconsumer()
#     print("1 --- test connect to db: " + test_connect_to_db())
#     print("2 --- test add delete consumer: " + test_add_delete_consumer())
