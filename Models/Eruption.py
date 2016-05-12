from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Eruption(Base):
    __tablename__ = "eruption"
    id = Column(Integer, primary_key=True,autoincrement=True)
    libelle = Column(String, nullable=False)
    duree = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=True)
    intensite = Column(float, nullable=True)
    

    def __init__(self,libelle,duree,date,intensite,id):
        self.id = id
        self.libelle = libelle
        self.duree = duree
        self.date = date
        self.intensite = intensite

    def __str__(self):
        return ("id : {};\nlibelle : {};\ndurée : {};\ndate : {};\nintensité : {}\n".format(self.id, self.libelle,self.duree,self.date,self.intensite))
