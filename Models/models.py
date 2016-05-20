from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///siteAstronomie.sqlite3', echo=False)

class Eclipse(Base):
    __tablename__ = "eclipse"
    id = Column(Integer, primary_key=True,autoincrement=True)
    libelle = Column(String, nullable=False)
    dateDeb = Column(DateTime, nullable=False)
    dateFin = Column(DateTime, nullable=True)
    pays = Column(String, nullable=True)
    departement = Column(String, nullable=True)
    type = Column(String, nullable=True)
    

    def __init__(self,libelle,dateDeb,dateFin,pays,departement,type):
        self.libelle = libelle
        self.dateDeb = dateDeb
        self.dateFin = dateFin
        self.pays = pays
        self.departement = departement
        self.type = type

    def __str__(self):
        return ("libelle : {};\ndate début : {};\ndate fin : {};\npays : {};\ndepartement : {};\ntype : {};\n".format(self.id, self.libelle,self.dateDeb,self.dateFin,self.pays,self.departement,self.type))

class Eruption(Base):
    __tablename__ = "eruption"
    id = Column(Integer, primary_key=True,autoincrement=True)
    libelle = Column(String, nullable=False)
    duree = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=True)
    intensite = Column(Float, nullable=True)
    

    def __init__(self,libelle,duree,date,intensite):
        self.libelle = libelle
        self.duree = duree
        self.date = date
        self.intensite = intensite

    def __str__(self):
        return ("libelle : {};\ndurée : {};\ndate : {};\nintensité : {}\n".format( self.libelle,self.duree,self.date,self.intensite))

class Evenement(Base):
    __tablename__ = "evenement"
    id = Column(Integer, primary_key=True,autoincrement=True)
    libelle = Column(String, nullable=False)
    dateDeb = Column(DateTime, nullable=False)
    dateFin = Column(DateTime, nullable=True)
    pays = Column(String, nullable=True)
    departement = Column(String, nullable=True)
    

    def __init__(self,libelle,dateDeb,dateFin,pays,departement):
        self.libelle = libelle
        self.dateDeb = dateDeb
        self.dateFin = dateFin
        self.pays = pays
        self.departement = departement
        

    def __str__(self):
        return ("libelle : {};\ndate début : {};\ndate fin : {};\npays : {};\ndepartement : {};\n".format(self.libelle,self.dateDeb,self.dateFin,self.pays,self.departement))

Base.metadata.create_all(engine)
