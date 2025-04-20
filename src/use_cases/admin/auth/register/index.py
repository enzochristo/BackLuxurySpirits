print(">>> carregando register_admin index")

from use_cases.admin.auth.register.register_admin_use_case import RegisterAdminUseCase
from repositories.user_repository import UsersRepository
from fastapi import FastAPI, Request, Response
from use_cases.admin.auth.register.register_dto import RegisterDTO
from fastapi import APIRouter
from entities.product import Product


router = APIRouter()

register_use_case = RegisterAdminUseCase(UsersRepository())

@router.post("/admin/auth/register")
def execute(register_dto:RegisterDTO, response:Response,request:Request):
    #executa a função dento do use case
    return register_use_case.execute(register_dto=register_dto,response=response,request=request) 