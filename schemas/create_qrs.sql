create table if not exists qrs
(
	id SERIAL,
	image_data BYTEA not null,
	user_id SERIAL references users(id)
);