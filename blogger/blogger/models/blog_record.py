import datetime
from .meta import Base
from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
)

from webhelpers2.text import urlify
from webhelpers2.date import distance_of_time_in_words

class BlogRecord(Base):

    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text(length=255), unique=True, nullable=False)
    body = Column(Text, default='')
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)


    @property
    def slug(self):
        return urlify(self.title)


    @property
    def created_in_words(self):
        return distance_of_time_in_words(self.created, datetime.datetime.utcnow())
