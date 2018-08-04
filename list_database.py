from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://postgres:admin@localhost/postgres')
db = scoped_session(sessionmaker(bind=engine))

def main():
	results = db.execute("SELECT * FROM flights").fetchall()
	for res in results:
		print(res)


if __name__ == '__main__':
	main()