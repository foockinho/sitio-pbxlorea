from decimal import Decimal

from sqlalchemy import Column, Sequence, String, Numeric, Float, Integer

from pbxcore.model import Base

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, Sequence('account_id_seq'), primary_key=True)
    name = Column(String(64))
    secret = Column(String(64))
    credit = Column(Numeric(16, 8), default=0.0)
    alias = Column(String(50))
    phone = Column(String(50))
    nonce = Column(Float, default=0.0)

    def __init__(self, secret):
        self.secret = secret
        self.credit = Decimal()
        self.alias = ""
        self.phone = ""

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.name, self.credit)

    def to_dict(self):
        data = {}
        data['name'] = str(self.name)
        data['credit'] = float(self.credit)
        data['number'] = str(self.phone)
        return data

