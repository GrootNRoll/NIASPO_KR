CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE some_table (
    id SERIAL PRIMARY KEY,
    field1 VARCHAR(255),
    field2 VARCHAR(255)
);

CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    action VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Пример данных
INSERT INTO users (username, password_hash) 
VALUES 
('user1', '5e884898da28047151d0e56f8dc6292773603d0d6aabbddbcc17773283510bc5'), -- "password"
('user2', '6cb75f652a9b52798eb6cf2201057c73e0671d473bf5f6cf57ed971c5c0f6e5e'); -- "password123"

INSERT INTO some_table (field1, field2) 
VALUES 
('example1', 'example2'), 
('example3', 'example4');
