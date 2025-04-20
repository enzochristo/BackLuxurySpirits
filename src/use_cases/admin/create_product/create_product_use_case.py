from repositories.product_repository import *
from entities.product import *
from fastapi import Request, Response
from .create_product_dto import CreateProductDTO

class CreateProductUseCase:
    def execute(self,create_product_dto:CreateProductDTO, response: Response, request:Request):
        if ((not create_product_dto.price) or (not create_product_dto.volume) or (not create_product_dto.stock) or (not create_product_dto.image) or (not create_product_dto.type)):
            response.status_code = 406 #codigo de informações faltantes
            return{"status": "error", "message": "Produto não cadastrado, pois falta informações"}
        
        if create_product_dto.type == "whisky":
            product = Whisky(**create_product_dto.model_dump(exclude={"type"}))
            WhiskiesRepository().save(product)
            return {"status": "success", "message": "Produto cadastrado com sucesso"}


        elif create_product_dto.type == "wine":
            product = Wine(**create_product_dto.model_dump(exclude={"type"}))
            WinesRepository().save(product)
            return {"status": "success", "message": "Produto cadastrado com sucesso"}


        elif create_product_dto.type == "beer":
            product = Beer(**create_product_dto.model_dump(exclude={"type"}))
            BeersRepository().save(product)
            return {"status": "success", "message": "Produto cadastrado com sucesso"}


        elif create_product_dto.type == "vodka":
            product = Vodka(**create_product_dto.model_dump(exclude={"type"}))
            VodkasRepository().save(product)
            return {"status": "success", "message": "Produto cadastrado com sucesso"}


        else:
            raise ValueError("Tipo de produto inválido")
        
        



        
        
        


