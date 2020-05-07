from sqlalchemy import create_engine,Column,String,Float,Integer,ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Atm(Base):
        __tablename__ = 'atm'
        id = Column('Account Number',Integer,primary_key=True)
        name = Column('Full Name',String,nullable=False)
        em = Column('Email Address',String,unique=True,nullable=True)
        bal = Column('Account Balance',Float,default=0.0)
        pin = Column('Secret Code',Integer,nullable=False)


engine = create_engine('sqlite:///atm.db')


if __name__ == '__main__':
        
    Base.metadata.create_all(bind=engine)
