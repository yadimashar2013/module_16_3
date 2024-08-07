from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
# uvicorn main:app --reload

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def post_user(
        username: Annotated[str, Path(min_length=3, max_length=20, discription='Enter username', example='UrbanUser')],
        age: int = Path(ge=18, le=120, discription='Enter age', example='24')) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(username: Annotated[str, Path(min_length=3, max_length=20, discription='Enter username', example='UrbanUser')],
                      user_id: int = Path(ge=1, le=20, discription='Enter id', example='3'),
                      age: int = Path(ge=18, le=120, discription='Enter age', example='24')) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is registered"


@app.delete('/user/{user_id}')
async def delite_user(user_id: str = Path(ge=1, le=20, discription='Enter id', example='3')) -> str:
    users.pop(user_id)
    return f"The user {user_id} is delite"



# @app.get('/user/{user_id}')
# async def user_id_(user_id: int = Path(ge=1, le=100, discription='Enter User ID', example='33')) -> dict:
#     return {"message": f'Вы вошли как пользователь № {user_id}'}
#
# @app.get('/user/{username}/{age}')
# async def user_username_(username: Annotated[str, Path(min_length=5, max_length=20, discription='Enter username', example='UrbanUser')],
#                          age: int = Path(ge=18, le=120, discription='Enter age', example='24')) -> dict:
#     return {"message": f'Информация о пользователе. Имя: {username}, Возраст: {age}'}