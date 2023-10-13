CREATE DATABASE travel_planner;
USE travel_planner;

CREATE TABLE User (
    user_id INTEGER PRIMARY KEY,
    password VARCHAR(255),
    name TEXT
);

CREATE TABLE Trip (
    trip_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    accommodation_id INTEGER, 
    destination_id INTEGER, 
    start_date VARCHAR(225),
    end_date VARCHAR(225),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (accommodation_id) REFERENCES Accommodation(accommodation_id),
    FOREIGN KEY (destination_id) REFERENCES Destination(destination_id)
);

CREATE TABLE Accommodation (
    accommodation_id INTEGER PRIMARY KEY,
    name TEXT,
    address VARCHAR(255)
);

CREATE TABLE Destination (
    destination_id INTEGER PRIMARY KEY,
    name TEXT,
    address VARCHAR(255)
);

CREATE TABLE Rooms (
    room_id INTEGER PRIMARY KEY,
    accommodation_id INTEGER,
    check_in VARCHAR(225),
    check_out VARCHAR(225),
    status VARCHAR(225),
    no_of_beds INTEGER,
    FOREIGN KEY (accommodation_id) REFERENCES Accommodation(accommodation_id)
);
