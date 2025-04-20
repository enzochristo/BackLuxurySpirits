from fastapi import Request, Response
from repositories.user_repository import UsersRepository
from repositories.product_repository import ProductRepository, WhiskiesRepository,BeersRepository, VodkasRepository, WinesRepository
from use_cases.buyer.add_to_cart.add_to_cart_dto import AddToCartDTO
from entities.cart_item import CartItem


class AddToCartUseCase:
    def __init__(self, user_repository:UsersRepository):
        self.user_repository = user_repository

    def execute(self, add_to_cart_dto:AddToCartDTO, response: Response, request: Request):
        if  not (add_to_cart_dto.product_id):
            response.status_code = 404
            return {"status":"Produto não encontrado","message":"Não foi possível adicionar ao carrinho por falta de informações"}
       
        user_id = request.state.auth_payload["user_id"]
        self.user_repository.add_product_to_cart(user_id= user_id, add_to_cart_dto=add_to_cart_dto)

        response.status_code = 201
        return {"status": "success", "message":"Produto adicionado ao carrinho!"}

