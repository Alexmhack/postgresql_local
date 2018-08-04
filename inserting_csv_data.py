from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import csv

engine = create_engine("postgresql://postgres:admin@localhost/postgres")
db = scoped_session(sessionmaker(bind=engine))

def main():
	csv_data = open('flights_data.csv')
	reader = csv.reader(csv_data)

	for origin, destination, duration in reader:
		db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
			{'origin': origin, 'destination': destination, 'duration': duration}
		)
		print(f"INSERTED:\n\t ORIGIN:{origin} DESTINATION: {destination} DURATION: {duration}")
	db.commit()


if __name__ == "__main__":
	main()