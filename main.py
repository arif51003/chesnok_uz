from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import status

from datetime import datetime
import random
import string

app = FastAPI()

user_db=dict()

def generate_str(ln):
    charac=string.ascii_letters+string.digits
    random_str="".join(random.choices(charac, k=ln))
    return random_str

@app.post("/users/create/")
def user_create():
    user_id = random.randint(1,100)
    name=generate_str(10)
    age=random.randint(1,50)
    is_active=random.choice([True,False])
    
    new_user={
        'id':user_id,
        "name": name,
        'age': age,
        'is_active': is_active,
        'create_at': datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        
    }
    
    user_db[user_id]=new_user
    return new_user

@app.get('/users/list')
def user_list():
    return user_db


@app.get("users/{user_id}")
def users_detail(user_id):
    try:
        return user_db[user_id]
    except KeyError:
        return JSONResponse(
            content={"error":"User not found"},status_code=404
        )
        
        
@app.put("/users/{user_id}/")
def  user_update(user_id):
    try:
        user=user_db[user_id]
        user["name"]=generate_str(8)
        user["age"]=random.randint(1,60)
        user_db[user_id]=user
        return user
    except KeyError:return JSONResponse(
                    content={"error":"User not found"},status_code=404
    )
    
@app.delete("users/{user_id}")
def user_del(user_id):
    try:
        del user_db[user_id]
        return JSONResponse(status_code=204)
    except KeyError:
        return JSONResponse(
            content={"error":"User not found"},status_code=404
        )