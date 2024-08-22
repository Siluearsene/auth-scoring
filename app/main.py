from fastapi import FastAPI
from app.api.routers.login import router as login_router
from app.configuration.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
import logfire
from app.api.routers.user import router as user_router


app = FastAPI(title="Authentication Microservice scoring credit")

Base.metadata.create_all(bind=engine)


origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/api/v1")
app.include_router(login_router, prefix="/api/v1")

# Configure logfire
logfire.configure(service_name='auth-microservice',)
logfire.info('Auth Microservice Started')



