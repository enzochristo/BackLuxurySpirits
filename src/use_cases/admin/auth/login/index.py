from use_cases.admin.auth.login.login_admin_use_case import LoginAdminUseCase
from repositories.user_repository import UsersRepository
from fastapi import FastAPI, Request, Response
from use_cases.admin.auth.login.login_dto import LoginDTO


from fastapi import APIRouter

router = APIRouter()

user_repository = UsersRepository()
login_use_case = LoginAdminUseCase(user_repository)

@router.post("/admin/auth/login") #colocamos a rota que vamos acessar no site
def execute(login_DTO:LoginDTO, response:Response,request:Request): #passamos os parametros para que seja possivel averiguar o login
    return login_use_case.execute(login_DTO,response,request=request)