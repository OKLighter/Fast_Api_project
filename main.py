"""
requirements
fastapi
pydantic
uvicorn
"""
from fastapi import FastAPI, Query
from schemas import Book

app = FastAPI()


# @app.get("/")
# def home():
#     return {"key": "Hello"}
#
#
# # uvicorn main:app --reload --port 8080 - запуск сервера
# # http://127.0.0.1:8000/docs - заходим на страницу
# # http://127.0.0.1:8000/redoc - автогенерация от redoc
#
# @app.get("/{pk}")
# def get_item(pk: int, q: str = None):
#     return {"key": pk, "q": q}
#
#
# # http://127.0.0.1:8080/docs снова заходим и видим новый url
# # http://127.0.0.1:8080/5, если ввести не int, то выдаст ошибку(если только один параметр pk, без q)
# # http://127.0.0.1:8080/5?q=hello --> {"key":5,"q":"hello"}
#
# @app.get('/user/{pk}/items/{item}/')
# def get_user_item(pk: int, item: str):
#     return {'user': pk, "item": item}
# # http://127.0.0.1:8080/user/5/items/tv/
#

@app.post('/book')
def create_book(item: Book):
    return item
# http://127.0.0.1:8080/docs - появится post/book, сразу показывает, тело пост запроса с типами данных


@app.get('/book')
def get_book(q: str = Query(None)):
    return q

