import hashlib
from sqlmodel import Session, select

from database import create_db_and_tables, engine
from models import Users, Bakeshop


def main():
    create_db_and_tables()

    user1 = Users(name='dave1234', password=hashlib.sha256('123'.encode()).hexdigest())
    user2 = Users(name='qwer', password=hashlib.sha256('1234'.encode()).hexdigest())

    with Session(engine) as session:
        session.add(user1)
        session.add(user2)
        session.commit()


if __name__ == "__main__":
    main()