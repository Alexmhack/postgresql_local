from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("postgresql://postgres:admin@localhost/postgres")
db = scoped_session(sessionmaker(bind=engine))

def main():
	result = db.execute("SELECT * FROM flights")
	for res in result:
		print(res)


def insert_flight(o, dest, dur):
	db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
		{'origin': o, 'destination': dest, 'duration': dur})
	db.commit()
	print(F"INSERTED:\n\tORIGIN: {o}  DESTINATION: {dest}  DURATION: {dur}")


def insert_passenger(name, flight):
	db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
		{'name': name, 'flight_id': flight})
	db.commit()
	print(F"INSERTED:\n\tNAME: {name}  FLIGHT ID: {flight}")


def delete_passenger(name):
	db.execute(f"DELETE FROM passengers WHERE name='{name}'")
	db.commit()


def delete_flight(flight_id):
	db.execute(f"DELETE FROM flights WHERE id = {flight_id}")
	db.commit()


if __name__ == "__main__":
	# insert_flight('Ladakh', 'Kabul', 180)
	# delete_flight(13)
	# insert_passenger('Ranbir', 13)
	# delete_passenger('Ranbir')
	main()