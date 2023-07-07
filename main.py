import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import json

from models import create_tables, Publisher, Book, Shop, Stock, Sale
from config import DB_URI


def create_db(data):
    DSN = DB_URI
    engine = sq.create_engine(DSN)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()

    session.close()


def fixtures_file():
    with open("fixtures/tests_data.json", encoding="utf-8") as file:
        file_data = json.load(file)
    return file_data


if __name__ == "__main__":
    create_db(fixtures_file())
