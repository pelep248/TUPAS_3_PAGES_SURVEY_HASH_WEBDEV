import hashlib
from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine
from fastapi.middleware.cors import CORSMiddleware

from models import Users, Bakeshop

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost:3000",  # React development server
    "https://example.com",    # Production frontend
    "*"
] # Define allowed origins (domains that can access your API)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow these origins
    allow_credentials=True,       # Allow cookies, authentication headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/{id}")
async def read_Users(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        user = session.get(Users, id)
        return {"message": user}
    

@app.post("/usersRegister")
async def root(users  : Users):
    with Session(engine) as session:
        users.password = hashlib.sha256(users.password.encode()).hexdigest()
        session.add(users)
        session.commit()
        session.refresh(users)
        return {
            "status":"success",
            "data": users
            }
    
@app.post("/usersLogin")
async def root(users  : Users):
    with Session(engine) as session:


        print()
        hashed_pass = hashlib.sha256(users.password.encode()).hexdigest()
        statement = select(Users).where(Users.name == users.name).where(Users.password == hashed_pass)
        results = session.exec(statement)

        # if(results)

        # print('-----------------------------')
        # print(Users.password , users.password)
        # print('-----------------------------')

        result = results.first()
        print(result)

        if (result == None):
            return {"status":"failed"}


        return {
            "status":"success",
            "data": result
            }
    
@app.get("/bakeshop/{id}")
async def read_Bakeshop(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        user = session.get(Bakeshop, id)
        return {"message": user}
    

@app.post("/bakeshop")
async def root(bakeshop  : Bakeshop):
    with Session(engine) as session:
        session.add(bakeshop)
        session.commit()
        session.refresh(bakeshop)
        return {
            "status":"success",
            "data": bakeshop
            }