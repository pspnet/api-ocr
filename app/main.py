import ddddocr
from typing import Optional

from fastapi import FastAPI, File

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


ocr = ddddocr.DdddOcr(show_ad=False, old=True)


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    code = ocr.classification(file)
    return {"code": code}
