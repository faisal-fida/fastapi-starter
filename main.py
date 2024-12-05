from fastapi import FastAPI
from routers import router
from fastapi.middleware.cors import CORSMiddleware
import utils.database  # noqa


# initialize app
app = FastAPI()

# add cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# initialize routes
app.include_router(router.router, prefix="/api", tags=["Application"])


# initialize base routes
@app.get("/")
def base_route():
    return {"msg": "Welcome to fastapi"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
