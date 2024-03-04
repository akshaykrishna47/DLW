SHOW DATABASES;
DROP DATABASE aaaa;
DROP TABLE Schedule;

CREATE DATABASE Data;
USE Data;
CREATE TABLE Schedule(
	room_no INT,
    date_ DATE,
    time_ INT,
    booking_status BOOL,
    PRIMARY KEY (room_no, date_, time_)
);
INSERT INTO Schedule (room_no, date_, time_, booking_status)
	VALUES
		('23','2024-03-04', '1200', TRUE),
		('23','2024-03-04', '1300', TRUE);

SELECT * FROM Schedule;


--     indoor_temperature INT,
--     outdoor_temperature INT,
--     weather STRING,