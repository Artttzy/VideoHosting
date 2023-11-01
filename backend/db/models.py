from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta

Base = declarative_base()

class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String)
    path = Column(String)