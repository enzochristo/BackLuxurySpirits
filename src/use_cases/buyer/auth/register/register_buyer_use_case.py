from repositories.user_repository import UsersRepository
from use_cases.buyer.auth.register.register_dto import RegisterDTO
from fastapi import Request, Response
from entities.user import User

class RegisterBuyerUseCase:
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    def execute(self, register_dto: RegisterDTO, response: Response, request: Request):
        if not register_dto.name or not register_dto.email or not register_dto.password:
            response.status_code = 406
            return {"status": "error", "message": "Cadastro não realizado, pois falta informações"}

        user = User(
            name=register_dto.name,
            email=register_dto.email,
            password=register_dto.password,
            type="buyer"
        )
        self.user_repository.save(user)

        response.status_code = 201
        return {"status": "success", "message": "Cadastro do comprador com sucesso"}
