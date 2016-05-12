from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Eclipse(Base):
    __tablename__ = "eclipse"
    id = Column(Integer, primary_key=True,autoincrement=True)
    libelle = Column(String, nullable=False)
    dateDeb = Column(DateTime, nullable=False)
    dateFin = Column(DateTime, nullable=True)
    pays = Column(String, nullable=True)
    departement = Column(String, nullable=True)
    type = Column(String, nullable=True)
    

    def __init__(self,libelle,dateDeb,dateFin,pays,departement,type,id):
        self.id = id
        self.libelle = libelle
        self.dateDeb = dateDeb
        self.dateFin = dateFin
        self.pays = pays
        self.departement = departement
        self.type = type

    def __str__(self):
        return ("id : {};\nlibelle : {};\ndate début : {};\ndate fin : {};\npays : {};\ndepartement : {};\ntype : {};\n".format(self.id, self.libelle,self.dateDeb,self.dateFin,self.pays,self.departement,self.type))
