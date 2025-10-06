CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

INSERT INTO products (name) VALUES ('Laptop'), ('Phone'), ('PC'), ('MP3-player'), ('Headphones');
