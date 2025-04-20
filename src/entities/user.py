import dotenv
from pydantic import BaseModel
from typing import Literal, List
from entities.product import *
from entities.cart_item import CartItem
dotenv.load_dotenv()

class User(BaseModel):
    _id: str
    name: str
    email: str
    password: str
    type: Literal["admin", "buyer"]
    cart: List[CartItem] = []
    reset_pwd_token: str = ""
    reset_pwd_token_sent_at: int = 0
