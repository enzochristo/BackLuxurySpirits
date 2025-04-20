from use_cases.buyer.add_to_cart.add_to_cart_use_case import AddToCartUseCase
from use_cases.buyer.add_to_cart.add_to_cart_dto import AddToCartDTO
from repositories.user_repository import UsersRepository
from fastapi import APIRouter, Request, Response, Depends
from middlewares.validate_user_auth_token import validate_user_auth_token

router = APIRouter()

add_to_cart_use_case = AddToCartUseCase(UsersRepository())

@router.post("/buyer/cart/add", dependencies=[Depends(validate_user_auth_token)])
def add_product(add_to_cart_dto: AddToCartDTO, response: Response, request: Request):
    return add_to_cart_use_case.execute(add_to_cart_dto, response, request)
