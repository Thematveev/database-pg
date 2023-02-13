create table if not exists users
(
	id SERIAL unique,
	email VARCHAR(30) unique not null,
	pwd VARCHAR(100) not null
);