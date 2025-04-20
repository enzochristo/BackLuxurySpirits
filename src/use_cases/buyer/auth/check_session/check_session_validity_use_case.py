from fastapi import Response, Request
from fastapi import FastAPI, Request, Response, APIRouter, Depends

class CheckSessionValidatyUseCase:
    def execute(self, response: Response, request: Request):
        return {"status":"success", "message": "Autenticação é válida para acessar a página do usuario"}