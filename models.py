from sqlmodel import Field, SQLModel

class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    password: str


class Bakeshop(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int | None = None
    gender: str
    fave_bread: str
    innings: str