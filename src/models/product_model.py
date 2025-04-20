from mongoengine import *
import datetime
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))


class ProductModel(Document):
    meta = {'allow_inheritance': True}
    name = StringField(required=True)
    price = FloatField(required=True, min_value=45.0)
    volume = IntField(required=True)
    stock = IntField(required=True)
    image = StringField(required=True)  


    @classmethod
    def get_fields(cls):
        return [field for field in cls._fields if field != "id"]

    
        



class WinesModel(ProductModel):
    brand = StringField(choices=["Miolo", "Salton", "Aurora"])

class BeersModel(ProductModel):
    brand = StringField(choices=["Heineken", "Skol", "Budweiser"])

class WhiskiesModel(ProductModel):
    brand = StringField(choices=["Johnnie Walker", "Jack Daniels", "Chivas"])

class VodkasModel(ProductModel):
    brand = StringField(choices=["Absolut", "Smirnoff", "Ciroc"])



