import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
	flights = db.execute("SELECT * FROM flights").fetchall()
	print(flights)


if __name__ == '__main__':
	main()