import os
from peewee import Model, MySQLDatabase, Proxy

db_proxy = Proxy()

def use_db():
    '''Use mysql instance to support models
    '''
    db_host = os.environ['DB_HOST']
    db_name = os.environ['DB_NAME']
    db_user_name = os.environ['DB_USER']
    db_password = os.environ['DB_PWD']
    database = MySQLDatabase(
        db_name,
        host=db_host,
        user=db_user_name,
        password=db_password
    )
    db_proxy.initialize(database)

class BaseModel(Model):

    class Meta(object):
        database = db_proxy
