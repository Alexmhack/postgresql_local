from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("postgres://postgres:admin@localhost/postgres")
db = scoped_session(sessionmaker(bind=engine))

result = db.execute("SELECT * FROM passengers")

def find_flight(name):
	result = db.execute(f"SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id WHERE name = '{name}'")
	for res in result:
		print(F"PASSENGER DETAILS\n\tPASSENGER NAME: {res.name}\n\tPASSENGER TRAVELLING FROM {res.origin} TO {res.destination}\n\tFLIGHT ID: {res.flight_id}\n\tFLIGHT DURATION: {res.duration}")


while True:
	name = input("Enter the name of the passenger: ")

	if name == 'exit':
		break

	if name in result.fetchall():
		find_flight(name)
	else:
		print("No passengers exists with that name...")

	find_flight(name)