from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Evenement(Base):
    __tablename__ = "evenement"
    id = Column(Integer, primary_key=True,autoincrement=True)
    libelle = Column(String, nullable=False)
    dateDeb = Column(DateTime, nullable=False)
    dateFin = Column(DateTime, nullable=True)
    pays = Column(String, nullable=True)
    departement = Column(String, nullable=True)
    

    def __init__(self,libelle,dateDeb,dateFin,pays,departement,id):
        self.id = id
        self.libelle = libelle
        self.dateDeb = dateDeb
        self.dateFin = dateFin
        self.pays = pays
        self.departement = departement
        

    def __str__(self):
        return ("id : {};\nlibelle : {};\ndate début : {};\ndate fin : {};\npays : {};\ndepartement : {};\n".format(self.id, self.libelle,self.dateDeb,self.dateFin,self.pays,self.departement))
