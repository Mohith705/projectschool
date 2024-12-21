from fastapi.security import HTTPBearer
from fastapi.exceptions import HTTPException
from fastapi import Request
from fastapi.security.http import HTTPAuthorizationCredentials
from src.db.redis import is_token_in_blocklist

class AccessTokenBearer(HTTPBearer):
    def __init__(self, auto_error=True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        credentials = await super().__call__(request)
        token = credentials.credentials
