from fastapi import APIRouter

from app.api.routers import user, login,user_predict

api_router = APIRouter()

api_router.include_router(login.router, prefix="/auth", tags=["auth"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(user_predict.router, prefix="/user_predict", tags=["user_predict"])
