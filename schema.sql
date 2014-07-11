DROP TABLE IF EXISTS forsale;
CREATE TABLE forsale(
	courseNum INTEGER(5),
	email TEXT NOT NULL,
	name TEXT NOT NULL,
	price DECIMAL(10,5)
);