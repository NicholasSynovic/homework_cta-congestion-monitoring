from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get(path="/")
def helloWorld() -> None:
    return {"msg": "Hello World"}
