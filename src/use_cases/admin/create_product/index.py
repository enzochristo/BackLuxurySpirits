from use_cases.admin.create_product.create_product_use_case import CreateProductUseCase
from repositories.product_repository import ProductRepository
from fastapi import FastAPI, Request, Response
from use_cases.admin.create_product.create_product_dto import CreateProductDTO
from fastapi import APIRouter


router = APIRouter()

create_product_use_case = CreateProductUseCase()

@router.post("/admin/create_product")
def execute(create_product_dto:CreateProductDTO, response: Response, request:Request):
    return create_product_use_case.execute(create_product_dto, response=response,request=request)
