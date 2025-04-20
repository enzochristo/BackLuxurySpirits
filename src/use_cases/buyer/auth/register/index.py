from fastapi import APIRouter, Response, Request
from repositories.user_repository import UsersRepository
from use_cases.buyer.auth.register.register_buyer_use_case import RegisterBuyerUseCase
from use_cases.buyer.auth.register.register_dto import RegisterDTO

router = APIRouter()
register_buyer_use_case = RegisterBuyerUseCase(UsersRepository())

@router.post("/auth/buyer/register")
def execute_buyer(register_dto: RegisterDTO, response: Response, request: Request):
    return register_buyer_use_case.execute(register_dto=register_dto, response=response, request=request)
