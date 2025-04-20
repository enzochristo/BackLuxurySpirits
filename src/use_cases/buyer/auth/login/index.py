from use_cases.buyer.auth.login.login_buyer_use_case import LoginBuyerUseCase
from use_cases.buyer.auth.login.login_dto import LoginDTO
from repositories.user_repository import UsersRepository
from fastapi import APIRouter
from fastapi import FastAPI, Request, Response

router = APIRouter()

user_repository = UsersRepository()

login_buyer_use_case = LoginBuyerUseCase(user_repository)

@router.post("/auth/buyer/login")
def login_buyer(login_DTO: LoginDTO, response: Response, request: Request):
    return login_buyer_use_case.execute(login_DTO, response=response, request=request)
