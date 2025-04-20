from pydantic import BaseModel
from typing import Literal 


class CreateProductDTO(BaseModel):
    name:str
    price: float
    volume: int
    stock: int
    image: str
    type: Literal["whisky", "wine", "beer", "vodka"]
    brand: str