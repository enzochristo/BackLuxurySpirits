from pydantic import BaseModel
from typing import Optional, Literal
from models.product_model import *

class Product(BaseModel):
    _id: str 
    name: str
    price: float
    volume: int
    stock: int
    image: str


class Wine(Product):
    brand: Literal["Miolo", "Salton", "Aurora"]
    _model_class = WinesModel


class Beer(Product):
    brand: Literal["Heineken", "Skol", "Budweiser"]
    _model_class = BeersModel


class Whisky(Product):
    brand: Literal["Johnnie Walker", "Jack Daniels", "Chivas"]
    _model_class = WhiskiesModel


class Vodka(Product):
    brand: Literal["Absolut", "Smirnoff", "Ciroc"]
    _model_class = VodkasModel