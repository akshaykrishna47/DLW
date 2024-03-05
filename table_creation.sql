SHOW DATABASES;
DROP DATABASE testdata;
DROP TABLE Schedule;

ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
CREATE DATABASE Data;
USE testdata;
CREATE TABLE Schedule(
	room_no INT,
    date_ DATE,
    time_ INT,
    booking_status INT,
    PRIMARY KEY (room_no, date_, time_)
);
INSERT INTO Schedule (room_no, date_, time_, booking_status)
	VALUES
		('23','2024-03-04', '1200', TRUE),
		('23','2024-03-04', '1300', TRUE);

SELECT * FROM Schedule;

CREATE TABLE stations (
    id TEXT PRIMARY KEY,
    device_id TEXT,
    name TEXT,
    latitude REAL,
    longitude REAL,
);

CREATE TABLE readings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    station_id TEXT,
    timestamp TEXT,
    value REAL,
    FOREIGN KEY (station_id) REFERENCES stations(id)
)




--     indoor_temperature INT,
--     outdoor_temperature INT,
--     weather STRING,