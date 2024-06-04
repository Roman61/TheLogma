from datetime import datetime
import time
from random import randint
import MySQLdb
import sqlalchemy

from DB_engine.EngineOfData.Consumer_db.Consumer_db import ConsumerDB
from DB_engine.EngineOfData.Shipment_db.Shipment_db import ShipmentDB
from DB_engine.EngineOfData.User_db.User_db import UserDB
from DB_engine.ModelOfData.Shipment_Table.shipment import Shipment
from faker import Faker

# class TestShipment:
#
# def __init__(self):
shipments = []


def test_connect_to_db():
    connect_str = "mysql://root:@192.168.5.220/warehouse"
    e_shipment = ShipmentDB(connect_str)
    assert e_shipment is not None


@staticmethod
def last_id_to_rang_writing_test(e_):
    e_s = e_.readall()
    e_s_id = 0
    if len(e_s) > 0:
        e_s_id = e_s[len(e_s) - 1]['id'] + 1
    rand_bgn = randint(e_s_id, e_s_id + 10)
    rand_end = randint(rand_bgn, rand_bgn + 50) + 1
    return rand_bgn, rand_end


def test_last_id():
    euser = ShipmentDB()
    all_ = euser.readall()
    assert euser.last_id == all_[len(all_) - 1]['id']


def test_add_delete_shipment():
    fake = Faker("ru_RU")

    def helper_range(digital):
        yield from range(1, digital)

    # connect_str = "mysql://root:@192.168.5.220/warehouse"
    e_shipment = ShipmentDB()
    e_consumer = ConsumerDB()
    e_user = UserDB()
    users = e_user.readall()
    consumers = e_consumer.readall()
    result = False

    #  try:
    shipment_s = []
    ids = last_id_to_rang_writing_test(e_shipment)
    for k in range(*ids):
        consumers_rnd_id = randint(0, len(consumers) - 1)
        usr_rnd_id = randint(0, len(users) - 1)
        shipment = Shipment()
        shipment.id = k  # randint(10, 20000)
        shipment.date = datetime.now()
        shipment.Consumer_id = consumers[consumers_rnd_id]['id']
        shipment.User_id = users[usr_rnd_id]['id']
        shipment_s.append(shipment)
    len_db_2 = len(e_shipment.readall())
    for i in shipment_s:
        e_shipment.add(index=i.id, date=i.date, user_id=i.User_id, consumer_id=i.Consumer_id)
        shipments.append(i)

    len_self = len(shipments)
    len_execute_db = len(e_shipment.readall())
    result = len_execute_db - len_db_2 == len_self
    assert result

    len_self = len(shipments)
    len_db_2 = len(e_shipment.readall())

    for i in shipments:
        e_shipment.delete(index=i.id)
    len_execute_db = len(e_shipment.readall())
    assert len_execute_db == len_db_2 - len_self


# def test_delete_shipment():
#     e_shipment = ShipmentDB()
#     len_db = len(e_shipment.readall())
#     e_shipment.delete(e_shipment.last_id)
#     len_execute_db = len(e_shipment.readall())
#     assert len_db - 1 == len_execute_db


# if __name__ == "__main__":
#     # test_shipment = TestShipment()
#     print("1 --- test connect to db: " + (test_connect_to_db()))
#     print("2 --- test add delete shipment: " + (test_add_delete_shipment()))
