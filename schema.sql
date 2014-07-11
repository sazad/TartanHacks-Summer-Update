DROP TABLE IF EXISTS textbooks;
CREATE TABLE textbooks(
	courseNum integer,
	email text NOT NULL,
	name text NOT NULL,
	price integer
);