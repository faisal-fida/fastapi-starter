from fastapi import FastAPI
from app.routers import item_router

# initialize app
app = FastAPI()


# initialize base routes
@app.get("/")
def base_route():
    return {"msg": "Welcome to fastapi"}


# intialize router

app.include_router(
    item_router.router,
    prefix="/items",
    tags=["Application"],
)
