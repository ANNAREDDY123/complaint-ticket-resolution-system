CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE agents(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(100)
);

CREATE TABLE complaints(
    id INTEGER PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    category VARCHAR(100),
    priority VARCHAR(50),
    status VARCHAR(50),
    agent_id INTEGER,
    created_at DATETIME
);

CREATE TABLE resolutions(
    id INTEGER PRIMARY KEY,
    ticket_id INTEGER,
    resolution_note TEXT,
    resolved_by VARCHAR(100),
    resolved_at DATETIME
);
