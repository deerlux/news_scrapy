# -*- coding: utf-8 -*
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class NewsDataDB:
    
    def __init__(self, user = '', password= '' , 
            hostname='localhost', dbname='news_data',dbms = 'postgres'):
        
        if dbms.lower() == 'postgres':
            engine_str = 'postgres://{0}:{1}@{2}/{3}'.format(user,
                    password, hostname, dbname)
        else:            
            raise AssertionError('Wrong dbms type: %s' % dbms)
        
        self.engine = sqlalchemy.create_engine(engine_str)

        Session = sessionmaker(bind = self.engine)
        self.session = Session()

        metadata = sqlalchemy.MetaData(bind = self.engine)
        Base = declarative_base(metadata)

        class NewsData(Base):
            __table__ = sqlalchemy.Table('news_data', metadata, 
                    autoload = True)
        
        self.NewsData = NewsData
        self.query = self.session.query
        self.add = self.session.add
        self.commit = self.session.commit
        self.rollback = self.session.rollback
        self.flush = self.session.flush
        self.close = self.session.close


