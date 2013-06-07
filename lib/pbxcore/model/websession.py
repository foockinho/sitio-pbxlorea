from sqlalchemy import DateTime, Column, Sequence, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

from pbxcore.model import Base
from datetime import datetime


class WebSession(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, Sequence('session_id_seq'), primary_key=True)
    session_id = Column(String(40))
    timestamp = Column(DateTime())
    account_id = Column(ForeignKey('accounts.id'))
    account = relationship("Account", backref=backref('sessions', order_by=id))

    def __init__(self, account, session_id):
        self.account = account
        self.session_id = session_id
        self.timestamp = datetime.now()


