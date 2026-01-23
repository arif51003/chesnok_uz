from fastapi import FastAPI,Response
from fastapi.responses import JSONResponse
from fastapi import status
import json
from pydantic import BaseModel

from datetime import datetime
import random
import string

app = FastAPI()

user_db=dict()
jfile="file.json"

def generate_str(ln):
    charac=string.ascii_letters+string.digits
    random_str="".join(random.choices(charac, k=ln))
    return random_str

def read():
    with open(jfile,"r") as f:
        return json.load(f)
    
def write(data):
    with open(jfile,"w") as f:
        return json.dump(data,f,indent=4)

@app.post("/users/create/")
def user_create():
    data=read()
    user_id = random.randint(1,100)
    name=generate_str(10)
    age=random.randint(1,50)
    is_active=random.choice([True,False])
    
    data[user_id]={
        'id':user_id,
        "name": name,
        'age': age,
        'is_active': is_active,
        'create_at': datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        
    }
    
    write(data)
    return data[user_id]

@app.get('/users/list')
def user_list():
    return read()


@app.get("/users/{user_id}")
def users_detail(user_id):
    try:
        a=read()
        b=a[user_id]
        return b
    except KeyError:
        return JSONResponse(
            content={"error":"User not found"},status_code=404
        )
        
        
@app.put("/users/{user_id}")
def  user_update(user_id):
    data=read()
    try:
        user=data[user_id]
        user["name"]=generate_str(8)
        user["age"]=random.randint(1,60)
        data[user_id]=user
        write(data)
        return data[user_id]
    except KeyError:return JSONResponse(
                    content={"error":"User not found"},status_code=404
    )
    
        
@app.delete("/users/{user_id}")
def user_del(user_id: int):
    data = read()
    try:
        del data[str(user_id)]
        write(data)
        return Response(status_code=204)
    except IndexError:
        return JSONResponse(
            content={"error":"Not found"},
            status_code=404
        )
        



def read():
    with open(jfile, "r") as f:
        return json.load(f)

def write(data):
    with open(jfile, "w") as f:
        json.dump(data, f, indent=4)

def gen_str(n=8):
    return "".join(random.choices(string.ascii_letters, k=n))


@app.get("/users")
def get_users():
    return read()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    data = read()
    key = str(user_id)

    if key not in data:
        return JSONResponse(
            content={"error": "User not found"},
            status_code=404
        )

    return data[key]


@app.get("/users/active")
def get_active_users():
    data = read()
    return {k: v for k, v in data.items() if v["is_active"]}


@app.post("/users")
def create_user():
    data = read()
    user_id = str(random.randint(100, 999))

    data[user_id] = {
        "id": int(user_id),
        "name": gen_str(),
        "age": random.randint(18, 60),
        "is_active": True,
        "created_at": datetime.now().isoformat()
    }

    write(data)
    return data[user_id]


@app.post("/users/inactive")
def create_inactive_user():
    data = read()
    user_id = str(random.randint(1000, 1999))

    data[user_id] = {
        "id": int(user_id),
        "name": gen_str(),
        "age": random.randint(18, 60),
        "is_active": False,
        "created_at": datetime.now().isoformat()
    }

    write(data)
    return data[user_id]


@app.post("/users/age/{age}")
def create_user_with_age(age: int):
    data = read()
    user_id = str(random.randint(2000, 2999))

    data[user_id] = {
        "id": int(user_id),
        "name": gen_str(),
        "age": age,
        "is_active": True
    }

    write(data)
    return data[user_id]


@app.put("/users/{user_id}")
def update_user(user_id: int):
    data = read()
    key = str(user_id)

    if key not in data:
        return JSONResponse(
            content={"error": "User not found"},
            status_code=404
        )

    data[key] = {
        "id": user_id,
        "name": gen_str(),
        "age": random.randint(18, 60),
        "is_active": True
    }

    write(data)
    return data[key]


@app.put("/users/{user_id}/reset")
def reset_user(user_id: int):
    data = read()
    key = str(user_id)

    if key not in data:
        return JSONResponse(
            content={"error": "User not found"},
            status_code=404
        )

    data[key]["name"] = "RESET"
    data[key]["age"] = 0
    data[key]["is_active"] = False

    write(data)
    return data[key]


@app.patch("/users/{user_id}/name")
def patch_name(user_id: int):
    data = read()
    key = str(user_id)

    if key not in data:
        return JSONResponse(
            content={"error": "User not found"},
            status_code=404
        )

    data[key]["name"] = gen_str()
    write(data)
    return data[key]


@app.patch("/users/{user_id}/toggle")
def toggle_active(user_id: int):
    data = read()
    key = str(user_id)

    if key not in data:
        return JSONResponse(
            content={"error": "User not found"},
            status_code=404
        )

    data[key]["is_active"] = not data[key]["is_active"]
    write(data)
    return data[key]
