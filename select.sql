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