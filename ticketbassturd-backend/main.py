from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def_read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/testing")
def read_test():
        return {"testing": "success"}