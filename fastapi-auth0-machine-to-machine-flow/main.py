from fastapi import FastAPI
from .routers import auth_router

# initialize app
app = FastAPI()

# initialize routes
app.include_router(auth_router.router, prefix="/auth", tags=["Auth0"])
