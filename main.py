from fastapi import FastAPI
from api import times, capital, math


app = FastAPI()
app.include_router(times.router, prefix='/api/time')
app.include_router(capital.router, prefix='/api/capital')
app.include_router(math.router, prefix="/api/math")


@app.get("/", tags=["get"])
def read_root():
    """
    Hello World!
    :return: "Test Project by FastAPI"
    """
    return "Test Project by FastAPI"

