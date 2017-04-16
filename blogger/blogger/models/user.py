import datetime
from .meta import Base
from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
)
from passlib.apps import custom_app_context as blogger_pwd_context


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text(length=255), unique=True, nullable=False)
    password = Column(Text(length=255), nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)


    def verify_password(self, password):
        if password == self.password:
            self.set_password(password)
        return blogger_pwd_context.verify(password, self.password)

    def set_password(self, password):
        password_hash = blogger_pwd_context.encrypt(password)
        self.password = password_hash