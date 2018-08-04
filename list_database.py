from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://postgres:admin@localhost/postgres')
db = scoped_session(sessionmaker(bind=engine))

result = engine.execute("SELECT * FROM flights")

for res in result:
	print(f"{res.origin} to {res.destination}, {res.duration}")