from repositories.user_repository import UsersRepository
from fastapi import Request, Response


class DeleteAdminUseCase:
    def __init__(self,user_repository: UsersRepository):
        self.user_repository = user_repository

    def execute(self, user_id:str, response: Response, request: Request):
        user = self.user_repository.find_by_id(id=user_id)
        try:
            user.delete()
            response.status_code = 200
            return {"status":"success","message": "Admin deletado com sucesso" }
        
        except Exception as e:

            response.status_code = 404  
            return {"status": "error", "message": "erro ao deletar avaliador"}

        