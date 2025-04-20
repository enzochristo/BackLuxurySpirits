import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.product import *
from models.product_model import *
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash



class ProductRepository:
    model_class = None  # a ser definido pelas subclasses

   # função que salva a entidade no banco de dados
    def save(self, entity):
        model = entity._model_class
        model_instance = model()
        entity_dict = entity.__dict__

        for field in model.get_fields():
            if field in entity_dict:
                model_instance[field] = entity_dict[field]

        model_instance.save()

    def stock_by_brand(self, brand):
        return sum([item.stock for item in self.model_class.objects(brand=brand)])

    def increase_stock_by_brand(self, brand, quantity):
        self.model_class.objects(brand=brand).update(inc__stock=quantity)

    def decrease_stock_by_brand(self, brand, quantity):
        self.model_class.objects(brand=brand).update(dec__stock=quantity)

    def find_by_name(self,name):
        return self.model_class.objects(name=name)
    
    def find_by_id(self,id):
        return self.model_class.objects(id=id).first()
    
    def get_name_by_id(self, id):
        return self.model_class.objects(id=id).first().name
    
    def get_product_by_id(self,id):
        return self.model_class.objects(id=id).first()
    
    def get_price_by_id(self,id):
        return self.model_class.objects(id=id).first()
    
    def check_type_by_id(self,id):
            #pega pelo id e verifica se é referente a cada uma dessas classes,
            #se for retorna o produto com esse repositorio, que vai pode acessar o models
         repository : ProductRepository
         for repository in [WinesRepository(),BeersRepository(),WhiskiesRepository(),VodkasRepository()]:
            product = repository.find_by_id(id=id)
            if product:
               return product    
            
    def update_price(self,id,new_price):
        product = self.check_type_by_id(id=id)
        product.price = new_price



class WinesRepository(ProductRepository):
    model_class = WinesModel

class BeersRepository(ProductRepository):
    model_class = BeersModel

class WhiskiesRepository(ProductRepository):
    model_class = WhiskiesModel

class VodkasRepository(ProductRepository):
    model_class = VodkasModel
