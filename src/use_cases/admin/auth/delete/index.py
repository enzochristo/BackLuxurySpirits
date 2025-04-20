from repositories.user_repository import *
from fastapi import FastAPI, Request, Response, APIRouter, Depends
from .delete_use_case import DeleteAdminUseCase
from middlewares.validate_user_auth_token import validate_user_auth_token

router = APIRouter()

user_repository = UsersRepository()
delete_admin_use_case = DeleteAdminUseCase(user_repository=user_repository)

@router.delete("auth/admin/delete/{user_id}", dependencies=[Depends(validate_user_auth_token)])
def execute(user_id:str, response:Response, request: Request):
    return delete_admin_use_case(user_id=user_id,response=response,request=request)
