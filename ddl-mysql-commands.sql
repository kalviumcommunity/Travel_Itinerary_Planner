CREATE databases travel_planner
USE travel_planner;
CREATE TABLE User (
    user_id INTEGER,
    password VARCHAR(255),
    name TEXT
);

CREATE TABLE Trip (
    trip_id INTEGER,
    user_id integer,
    acommodation_id integer , 
    destination_id integer , 
    start_date varchar(225),
    end_date varchar(225)
);

CREATE TABLE Acommodation(
    acommodation_id INTEGER,
	name TEXT,
    address VARCHAR(255)
   
);

CREATE TABLE Destination (
    destination_id INTEGER,
    name TEXT,
    address VARCHAR(255)
);

CREATE TABLE Rooms (
    room_id INTEGER,
    acommodation_id integer , 
    check_in varchar(225),
    check_out varchar(225),
    status varchar(225),
    no_of_beds integer
);


