'''
logma - digital warehouse
virtual logistics man

The-Logma
The Logma - Warehouse and transportation support system.
Components: digital warehouse, virtual logistics, logistics management,
reporting, monitoring, document flow, event calendar.

'''

from DB_engine.EngineOfData.AbstractDataEngine import AbstractDataEngine
from DB_engine.ModelOfData.User_Table.User import User

def filter_attribyte(attr):
    if attr[:3] != '__' and attr[-2:] != '__':
        return True
    else:
        return False


def main():
    connect_str = "mysql://root:@192.168.5.220/warehouse"
    usr = User()

    euser = AbstractDataEngine(connect_str, usr)

    usr = euser.readone(index=2)
    print(usr)
   # euser.readone(2)


main()
