from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

#A ideia do carrinho é que seja uma classe, 
# pois teremos controle de quantos produtos foram add
#Assim, se forem produtos iguais, teremos a contagem pelo nome.


class CartsItem(EmbeddedDocument):
    product_id = StringField(required=True)   # ID do produto no catálogo
    previous_price = FloatField(required=True,default=0)         # Preço fixado no momento da adição


