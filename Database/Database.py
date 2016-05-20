import os.path
import csv
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from Exceptions.ErrorTypeException import ErrorTypeException
from Exceptions.DatabaseConnectionException import DatabaseConnectionException
from Models.models import *

class Database:
    """
    Classe intéractions base de données
    """

    def __init__(self, dbName="siteAstronomie.sqlite3"):
        self.dbName = dbName
        self.session = None
        if not os.path.isfile(dbName):
            raise DatabaseConnectionException("Erreur de connexion à la base de données : \nErreur détectée : {} n'existe pas\n".format(dbName))
        try:
            engine = create_engine('sqlite:///' + dbName, echo=True)
            Session = sessionmaker(bind=engine)
            self.session = Session()
        except Exception as err:
            raise DatabaseConnectionException('Erreur de connexion à la base de données :\nErreur détectée :\n%s' % err)

    def __str__(self):
        s = ''
        for event in self.session.query(Evenement):
            s = s + str(event) + "\n"
        for eclipse in self.session.query(Eclipse):
            s = s + str(eclipse) + "\n"
        for eruption in self.session.query(Eruption):
            s = s + str(eruption) + "\n"
        return s
    
    def create(self, obj, type):
        if isinstance(obj, type):
            self.session.add(obj)
            self.session.commit()
            return obj
        else:
            raise ErrorTypeException("Type inconnu")

    def delete(self, obj, type):
        if isinstance(obj, type):
            for obj in self.session.query(type).filter(type.id == obj.id):
                print()
                self.session.delete(obj)
            self.session.commit()
        else:
            raise ErrorTypeException("Type inconnu")

    def update (self):
        self.session.commit()

    def retrieve(self,type, column=None, value=None):
        if value != None:
            obj = self.session.query(type).filter(column == value).first()
            if obj != None:
                return obj
            return None
        else:
            obj = self.session.query(type).all()
            return obj
