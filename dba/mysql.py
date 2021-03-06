import pymysql
from sqlalchemy import DateTime, Integer, String, Float, create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

def insert_price(config, df):
  # 创建数据库连接
  engine = init_connect(config)
  con = engine.connect()
  # 将df数据插入数据库
  df.to_sql(name='price', con = con, if_exists = 'append', index=False)

def select_price(config, Pname, Pdate):
  engine = init_connect(config)
  Base = declarative_base(engine)
  session = sessionmaker(engine)()

  class Price(Base):
    __tablename__ = 'price'
    id = Column(Integer , primary_key=True , autoincrement=True)
    date = Column(DateTime)
    market_name = Column(String(64))
    vegetable = Column(String(64))
    low = Column(Float)
    high = Column(Float)

  db_data = session.query(Price).filter(Price.vegetable.like(f'%{Pname}%')).filter(Price.date == Pdate).all()
  return db_data

def insert_market(config, df):
  # 创建数据库连接
  engine = init_connect(config)
  con = engine.connect()
  # 将df数据插入数据库
  df.to_sql(name='market', con = con, if_exists = 'append', index=False)

def select_market(config, Mname):
  engine = init_connect(config)
  Base = declarative_base(engine)
  session = sessionmaker(engine)()

  class Market(Base):
    __tablename__ = 'market'
    id = Column(Integer , primary_key=True , autoincrement=True)
    market_id = Column(Integer)
    name = Column(String(64))

  db_data = session.query(Market).filter(Market.name.like(f'%{Mname}%')).all()
  return db_data

def select_null_market(config):
  engine = init_connect(config)
  Base = declarative_base(engine)
  session = sessionmaker(engine)()

  class Market(Base):
    __tablename__ = 'market_null'
    id = Column(Integer , primary_key=True , autoincrement=True)
    market_id = Column(Integer)
    name = Column(String(64))

  db_data = session.query(Market).filter().all()
  return db_data

def insert_null_market(config, df):
  # 创建数据库连接
  engine = init_connect(config)
  con = engine.connect()
  # 将df数据插入数据库
  df.to_sql(name='market_null', con = con, if_exists = 'append', index=False)

def init_connect(config):
  USERNAME = config['user']
  PASSWORD = config['password']
  HOST = config['host']
  PORT = config['port']
  DB = config['database']
  # 创建数据库连接
  engine = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}')
  return engine