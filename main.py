'''
logma - digital warehouse
virtual logistics man

The-Logma
The Logma - Warehouse and transportation support system.
Components: digital warehouse, virtual logistics, logistics management,
reporting, monitoring, document flow, event calendar.

'''

from DB_engine.EngineOfData.UsniversalDataEngine import UsniversalDataEngine
from DB_engine.EngineOfData.User_db.User_db import UserDB
from DB_engine.ModelOfData.User_Table.User import User


def filter_attribyte(attr):
    if attr[:3] != '__' and attr[-2:] != '__':
        return True
    else:
        return False


def main():
    connect_str = "mysql://root:@192.168.5.220/warehouse"
    usr = User()
    # , usr
    euser = UserDB(connect_str)
    ude = UsniversalDataEngine(data_obj=usr)

    usr = ude.readone(index=1)
    usr_name = usr.Name
    usr_last_name = usr.LastName
    usr_last_enter = usr.LastEnter
    usr_loggin = usr.Loggin
    usr_pass = usr.Pass
    usr_role = usr.Role
    print(usr_name)
    print(usr_last_name)
    print(usr_last_enter)
    print(usr_loggin)
    print(usr_pass)
    print(usr_role)

    usr.id = 1
    usr.Name = usr_name
    usr.LastName = usr_last_name
    usr.LastEnter = usr_last_enter
    usr.Loggin = usr_loggin
    usr.Pass = usr_pass
    usr.Role = 2

    ude.delete(usr.id)
    ude.add(usr)

    usr = ude.readall()[0]
    usr_name = usr.Name
    usr_last_name = usr.LastName
    usr_last_enter = usr.LastEnter
    usr_loggin = usr.Loggin
    usr_pass = usr.Pass
    usr_role = usr.Role
    print(usr_name)
    print(usr_last_name)
    print(usr_last_enter)
    print(usr_loggin)
    print(usr_pass)
    print(usr_role)


    pass
    # index, name, lastname, last_enter, loggin, password, role

    # usr = euser.readone(index=1)
    # print(type(usr[0]), *usr[0])
    #
    # euser.delete(index=1)
    # euser.add(index=usr[0]['id'],
    #           name=usr[0]['Name'],
    #           lastname=usr[0]['LastName'],
    #           last_enter=usr[0]['LastEnter'],
    #           loggin=usr[0]['Loggin'],
    #           password=usr[0]['Pass'],
    #           role=usr[0]['Role'])
    # usr = euser.readone(index=1)
    # print(*usr[0])


# euser.readone(2)


main()
