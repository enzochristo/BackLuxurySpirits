import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.user import User
from models.user_model import UsersModel
from repositories.product_repository import ProductRepository
from entities.cart_item import CartItem
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash
from models.cart_item_models import CartsItem

class UsersRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, user: User) -> None:
        user_model = UsersModel()
        user_dict = user.model_dump()

        for k in UsersModel.get_normal_fields():
            if (k not in user_dict):
                continue

            user_model[k] = user_dict[k]

        for k in UsersModel.sensivity_fields:
            user_model[k] = SensivityField(fernet=self.fernet, data=user_dict[k])

        user_model.password = bcrypt.hashpw(f'{user.password}'.encode(), bcrypt.gensalt()).decode()

        user_model.save()
        print(">>> Salvando usuário:", user_dict)


        return None
    
    def find_by_email(self, email: str) -> list[UsersModel]:
        result = UsersModel.objects(email=email)
        return result
    
    def find_by_id(self, id: str) -> list[UsersModel]:
        result = UsersModel.objects(id=id)[0]
        return result
    
    def update_reset_pwd_token(self, email: str, sent_at: int, token: str) -> None:
        UsersModel.objects(email=email).update(set__reset_pwd_token_sent_at=sent_at, set__reset_pwd_token=token)

        return None
    
    def find_by_reset_pwd_token(self, token) -> list[UsersModel]:
        result: list[UsersModel] = UsersModel.objects(reset_pwd_token=token)

        return result
    
    def update_pwd(self, id: str, pwd: str) -> None:
        UsersModel.objects(id=id).update(set__password = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode())

        return None
    
    def get_name(self, id: str) -> str:
        user = UsersModel.objects(id=id).first()
        if user:
            return user.name

    def get_email(self, id: str) -> str:
        user = UsersModel.objects(id=id).first()
        if user:
            return user.email
    
    def update_name(self, id: str, name: str) -> None:
        UsersModel.objects(id=id).update(set__name = name)
        return None

    def update_email(self, id: str, email: str) -> None:
        UsersModel.objects(id=id).update(set__email = email)
        return None
    
    def add_product_to_cart(self,user_id,add_to_cart_dto):
        user = self.find_by_id(id=user_id) #tem que buscar o user pelo id, não podemos simplesmente criar um usuario do zero
        product_repository = ProductRepository() #acessando o product repository para fazer uso dos dados do banco de dados 
        product = product_repository.check_type_by_id(id=add_to_cart_dto.product_id)

        if product.price != add_to_cart_dto.previous_price:
            previous_price = add_to_cart_dto.previous_price
        else:
            previous_price = product.price

        #Usando o pydantic, temos que passar sempre os atributos obrigatórios já ao definir o codiog
        #Caso contrario, vamos estar fazendo uso de uma classe que não tem seus requisitos minimos
        #preenchidos, por conta do models. Então, sempre definir da forma abaixo.
        cart_item = CartsItem(
            product_id=str(product.id),
            previous_price= previous_price
        ) #criamos a classe cart item para passar as informações para ele
       
            
        user.cart.append(cart_item)
        user.save()

    def check_price_by_id(self,id):
        user = self.find_by_id(id=id)
        item:CartItem
        product_repository = ProductRepository()
        for item in user.cart:
            product_id = item.product_id
            new_price =  product_repository.check_type_by_id(product_id).price
            if new_price != item.previous_price:
                message = f"O preço foi atualizado após a adição do carrinho, agora o novo preço é {new_price}"
                return message
        return None



    
        

    

        


        

