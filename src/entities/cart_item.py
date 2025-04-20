import dotenv
from pydantic import BaseModel
from typing import Literal, Optional, List
dotenv.load_dotenv()


# O carrinho será composto por itens do carrinho
class CartItem(BaseModel):
    product_id: str
    previous_price: float
