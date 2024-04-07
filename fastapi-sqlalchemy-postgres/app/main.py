from fastapi import FastAPI

# initialize app
app = FastAPI()


# initialize base routes
@app.get("/")
def base_route():
    return {"msg": "Welcome to fastapi"}