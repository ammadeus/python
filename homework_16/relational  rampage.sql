CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    user_type VARCHAR(10)
);

CREATE TABLE Rooms (
    room_id INT PRIMARY KEY,
    host_id INT,
    max_capacity INT,
    price DECIMAL(10, 2),
    has_ac VARCHAR(3),
    has_refrigerator VARCHAR(3),
    other_room_attributes TEXT,
    FOREIGN KEY (host_id) REFERENCES Users(user_id)
);

CREATE TABLE Reservations (
    reservation_id INT PRIMARY KEY,
    guest_id INT,
    room_id INT,
    check_in_date DATE,
    check_out_date DATE,
    FOREIGN KEY (guest_id) REFERENCES Users(user_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);

CREATE TABLE Reviews (
    review_id INT PRIMARY KEY,
    guest_id INT,
    room_id INT,
    rating INT,
    comment TEXT,
    FOREIGN KEY (guest_id) REFERENCES Users(user_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);


INSERT INTO Users (user_id, first_name, last_name, user_type)
VALUES
(1, 'Marco', 'Rossi', 'Host'),
(2, 'Anna', 'Bianchi', 'Guest'),
(3, 'Luca', 'Verdi', 'Host');


INSERT INTO Rooms (room_id, host_id, max_capacity, price, has_ac, has_refrigerator, other_room_attributes)
VALUES
(1, 1, 4, 100.00, 'Yes', 'Yes', 'Spacious and well-lit'),
(2, 1, 2, 75.00, 'No', 'Yes', 'Cozy and comfortable'),
(3, 2, 6, 150.00, 'Yes', 'No', 'Ideal for family vacations');


INSERT INTO Reservations (reservation_id, guest_id, room_id, check_in_date, check_out_date)
VALUES
(1, 2, 1, '2023-08-20', '2023-08-25'),
(2, 1, 2, '2023-09-10', '2023-09-15'),
(3, 3, 3, '2023-07-05', '2023-07-10');


INSERT INTO Reviews (review_id, guest_id, room_id, rating, comment)
VALUES
(1, 2, 1, 5, 'Beautiful room, wonderful experience!'),
(2, 1, 2, 4, 'Cozy and comfortable.'),
(3, 3, 3, 4, 'Enjoyable stay, spacious and clean.');

SELECT U.user_id, U.first_name, U.last_name
FROM Users U
JOIN Reservations R ON U.user_id = R.guest_id
GROUP BY U.user_id, U.first_name, U.last_name
ORDER BY COUNT(R.reservation_id) DESC
LIMIT 1;

