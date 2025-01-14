from fastapi import FastAPI



app = FastAPI()

@app.get("/")
async def home_page():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def page_admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def id_user(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def info(username: str, age: int) -> dict:
    return {"Информация о пользователе. Имя:": {username}, "Возраст:": {age}}