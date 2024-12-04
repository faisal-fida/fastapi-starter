from fastapi import FastAPI
from routers import auth_router
from routers import item_router
import utils.database  # noqa


# initialize app
app = FastAPI()

# initialize routes
app.include_router(auth_router.router, prefix="/auth", tags=["Auth0"])
app.include_router(item_router.router, prefix="/items", tags=["Application"])


# initialize base routes
@app.get("/")
def base_route():
    return {"msg": "Welcome to fastapi"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
