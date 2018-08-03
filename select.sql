SELECT * FROM flights;

SELECT origin, destination FROM flights;

SELECT * FROM flights WHERE id = 3;

SELECT * FROM flights WHERE origin = 'Indore';

SELECT destination, duration FROM flights WHERE destination = 'Italy';

SELECT * FROM flights WHERE duration > 500;

SELECT * FROM flights WHERE origin = 'Mumbai' AND duration < 200;

SELECT * FROM flights WHERE origin = 'Indore' OR duration > 500;

SELECT AVG(duration) FROM flights;

SELECT AVG(duration) FROM flights WHERE origin = 'Indore';

SELECT COUNT(*) FROM flights;

SELECT COUNT(*) FROM flights WHERE origin = 'Indore';

SELECT MIN(duration) FROM flights;

SELECT MAX(duration) FROM flights;

SELECT * FROM flights WHERE duration = 120;

SELECT * FROM flights WHERE origin IN ("Indore", "New York");

SELECT * FROM flights WHERE origin LIKE '%a%';

SELECT * FROM flights WHERE origin LIKE '%New%';

SELECT * FROM flights LIMIT 2;

SELECT * FROM flights ORDER BY duration ASC;

SELECT * FROM flights ORDER BY duration ASC LIMIT 2;

SELECT * FROM flights ORDER BY duration DESC;

SELECT * FROM flights ORDER BY duration DESC LIMIT 2;

SELECT origin, COUNT(*) FROM flights GROUP BY origin;

SELECT origin, COUNT(*) FROM flights GROUP BY origin ORDER BY COUNT(*) ASC;

SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;

SELECT * FROM passengers WHERE name='Pranav';

SELECT * FROM flights WHERE id = 4;

SELECT passengers.name, flights.origin, flights.destination, flights.duration
	FROM passengers JOIN flights ON passengers.flight_id = flights.id;

SELECT * FROM passengers JOIN flights ON passengers.flight_id = flights.id;

SELECT name, origin, destination FROM flights 
	JOIN passengers ON passengers.flight_id = flights.id;

SELECT name, origin, destination FROM flights 
	JOIN passengers ON passengers.flight_id = flights.id WHERE name = 'Pranav';

SELECT name, origin, destination FROM flights 
	JOIN passengers ON passengers.flight_id = flights.id ORDER BY duration;

SELECT name, origin, destination, duration FROM flights
	JOIN passengers ON passengers.flight_id = flights.id ORDER BY name LIMIT 5;

SELECT name, origin, destination, duration FROM flights
	LEFT JOIN passengers ON passengers.flight_id = flights.id;