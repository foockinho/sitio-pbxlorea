from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Sequence, Numeric, DateTime, Float, ForeignKey, Text, Boolean, Enum, BigInteger

from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from datetime import datetime
import time

from decimal import Decimal

from pbxcore.config import config
from datetime import datetime

#######################################################
# Model Declaration

from pbxcore.model.account import Account
from pbxcore.model.websession import WebSession

#######################################################
# Nasty database initialization stuff

# only one per application for thread-local storage
# http://docs.sqlalchemy.org/en/latest/orm/session.html#unitofwork-contextual
cfg = config['db']
user = cfg['user']
password = cfg['password']
host = cfg.get('host', 'localhost')
database = cfg['database']
engine = create_engine('mysql://%s:%s@%s/%s' % (user, password, host, database), pool_size=15)
# set types on the db tables in case we're creating
for a in [Account, WebSession]:
    a.__table__.mysql_engine = 'InnoDB'
    a.__table__.mysql_charset = 'utf8'

Base.metadata.create_all(engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# Another thing to be aware of us the pool_size of the connection pool, which is 5 by default. For many applications that's fine, but if you are creating lots of threads, you might need to tune that parameter
# http://stackoverflow.com/questions/9619789/sqlalchemy-proper-session-handling-in-multi-thread-applications

#######################################################
# Helper object to ensure we use sqlalchemy in threaded way

class Model(object):
    def __init__(self):
        #engine.execute("CREATE DATABASE alchemy")
        #engine.execute("USE dbname")
        #engine =create_engine('sqlite:///:memory:', echo=False)
        #Session.configure(bind=self._engine)  # once engine is available
        self.session = Session()

    def query(self, *args, **kargs):
        return self.session.query(*args, **kargs)
