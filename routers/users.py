from fastapi import APIRouter

class UserRouter(APIRouter):

    def __init__(self, prefix: str = "/api/v1/user") -> None:
        
        super().__init__(prefix=prefix, tags=[])
        super().add_api_route(path="/login", endpoint=self.test, methods=["GET"])

    async def test(self) -> dict:
        return {"message": "Test route works"}