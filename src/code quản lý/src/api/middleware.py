# Placeholder for middleware, e.g., authentication middleware
from fastapi import Request, HTTPException
from python_jose import jwt, JWTError
from src.config import Config

async def jwt_middleware(request: Request, call_next):
    token = request.headers.get("Authorization")
    if token:
        try:
            token = token.replace("Bearer ", "")
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[ "HS256" ])
            request.state.user_id = payload.get("user_id")
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")
    response = await call_next(request)
    return response