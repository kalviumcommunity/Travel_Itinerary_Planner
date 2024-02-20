use travel_planner;
show tables;

-- INSERTING data's to the table
INSERT INTO User (user_id, password, name) VALUES (1, 'user123', 'John Doe');
INSERT INTO Trip (trip_id, user_id, accommodation_id, destination_id, start_date, end_date) VALUES (1, 1, 2, 3, '2023-10-15', '2023-10-20');
INSERT INTO accommodation (accommodation_id, name, address) VALUES (2, 'Hotel XYZ', '123 Main St');
INSERT INTO accommodation (accommodation_id, name, address) VALUES (7, 'motel XYZ', '123 paris');
INSERT INTO Destination (destination_id, name, address) VALUES (3, 'City ABC', '456 Elm St');
INSERT INTO Rooms (room_id, check_in, check_out, status, no_of_beds)VALUES (1,  '2023-10-15', '2023-10-20', 'Available', 2);


-- Update Data in Tables

UPDATE User SET name = 'Jane Doe' WHERE user_id = 1;
UPDATE Trip SET start_date = '2023-11-01', end_date = '2023-11-05' WHERE trip_id = 1;
UPDATE Rooms SET status = 'Occupied' WHERE room_id = 1;

-- Delete Data from Tables

DELETE FROM User WHERE user_id = 1;
DELETE FROM Trip WHERE trip_id = 1;
DELETE FROM Rooms WHERE room_id = 1;

-- example
-- 1. decending oder by accommodation_id
select * from accommodation order by accommodation_id DESC

-- 2. to find total number of accommodation per city

select SUBSTRING_INDEX(address, ' ', -1) AS city,
       count(*) AS accommodation_count
from accommodation
group by  city;



