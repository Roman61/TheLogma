from datetime import datetime
import time
from random import randint
import MySQLdb
import sqlalchemy


from DB_engine.EngineOfData.Provider_db.Provider_db import ProviderDB
from DB_engine.ModelOfData.Provider_Table.provider import Provider
from DB_engine.EngineOfData.User_db.User_db import UserDB
from DB_engine.ModelOfData.User_Table.User import User
from DB_engine.ModelOfData.Delivery_Table.delivery import Delivery
from DB_engine.EngineOfData.Delivery_db.Delivery_db import DeliveryDB
from faker import Faker

# class TestShipment:
#
# def __init__(self):
deliverys = []


def test_connect_to_db():
    e_delivery = DeliveryDB()
    assert e_delivery is not None


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
    e_delivery = DeliveryDB()
    all_ = e_delivery.readall()
    id_ = all_[len(all_) - 1]['id']
    assert e_delivery.last_id == id_


def test_add_delete_delivery():

    e_delivery = DeliveryDB()

    e_provider = ProviderDB()
    e_user = UserDB()

    users = e_user.readall()
    providers = e_provider.readall()

    delivery_s = []
    ids = last_id_to_rang_writing_test(e_delivery)
    for k in range(*ids):
        consumers_rnd_id = randint(0, len(providers) - 1)
        usr_rnd_id = randint(0, len(users) - 1)
        delivery = Delivery()
        delivery.id = k
        delivery.Date = datetime.now()
        delivery.Provider_id = providers[consumers_rnd_id]['id']
        delivery.User_id = users[usr_rnd_id]['id']
        delivery_s.append(delivery)
    len_db_2 = len(e_delivery.readall())
    for i in delivery_s:
        e_delivery.add(index=i.id, date=i.Date, user_id=i.User_id, provider_id=i.Provider_id)
        deliverys.append(i)

    len_self = len(deliverys)
    len_execute_db = len(e_delivery.readall())
    result = len_execute_db - len_db_2 == len_self
    assert result

    len_self = len(deliverys)
    len_db_2 = len(e_delivery.readall())

    for i in deliverys:
        e_delivery.delete(index=i.id)
    len_execute_db = len(e_delivery.readall())
    assert len_execute_db == len_db_2 - len_self












