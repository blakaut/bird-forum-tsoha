CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    bio VARCHAR(50),
    authority SMALLINT
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES categories,
    user_id INTEGER REFERENCES users,
    content TEXT
);

CREATE TABLE replies (
    id SERIAL PRIMARY KEY,
    content TEXT,
    thread_id INTEGER REFERENCES threads,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);

CREATE TABLE privateMessages (
    id SERIAL PRIMARY KEY,
    sender INTEGER REFERENCES users,
    recipient INTEGER REFERENCES users,
    seen BOOLEAN
);

INSERT INTO categories (name) values ('Parrots');
INSERT INTO categories (name) values ('Ioras');
INSERT INTO categories (name) values ('Storks');
INSERT INTO categories (name) values ('Shorebirds');