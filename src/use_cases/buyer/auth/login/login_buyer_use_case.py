from repositories.user_repository import UsersRepository
from fastapi import Request, Response
from use_cases.buyer.auth.login.login_dto import LoginDTO
import jwt
import os

class LoginBuyerUseCase:
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    def execute(self, login_DTO: LoginDTO, response: Response, request: Request):
        check_exists = self.user_repository.find_by_email(email=login_DTO.email)

        if not check_exists:
            response.status_code = 404
            return {"status": "error", "message": "Não foi possível achar um comprador com o email fornecido"}
        
        user = check_exists[0]

        if not user.check_password_matches(login_DTO.password):
            response.status_code = 403
            return {"status": "error", "message": "Senha incorreta"}

        token = jwt.encode(
            {"email": user.email, "id": str(user.id), "user_type": user.type},
            os.getenv("USER_JWT_SECRET")
        )

        response.set_cookie(key="user_auth_token", value=f"Bearer {token}", httponly=True)

        response.status_code = 202
        return {"status": "success", "message": "Login realizado com sucesso"}
