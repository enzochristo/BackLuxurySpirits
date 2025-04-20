print(">>> carregando register_admin_use_case")

from repositories.user_repository import UsersRepository
from use_cases.admin.auth.register.register_dto import RegisterDTO
from fastapi import Request, Response
from entities.user import User


class RegisterAdminUseCase:
    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    def execute(self,register_dto: RegisterDTO, response:Response, request:Request):
        if not register_dto.name or not register_dto.email or not register_dto.password: #verificar se está com as infos completas
            response.status_code = 406
            return{"status": "error", "message": "Cadastro não realizado, pois falta informações"}

        user = User(
              name=register_dto.name,
              email=register_dto.email,
              password=register_dto.password,
              type="admin"
           ) 
        #agora para salvar no banco de dados usamos o repository 
        self.user_repository.save(user)

        response.status_code = 201

        return{"status": "success", "message": "Cadastro do admin com sucesso"}
    
        
        
