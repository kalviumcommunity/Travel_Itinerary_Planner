class User:
    def __init__(self, username, password):
        self.user_id = self.get_next_user_id()
        self.username = username
        self.password = password
        self.trips = []

    @staticmethod
    def get_next_user_id():
        try:
            with open("user_id.txt", "r") as file:
                user_id = int(file.read())
        except FileNotFoundError:
            user_id = 1
        with open("user_id.txt", "w") as file:
            file.write(str(user_id + 1))
        return user_id

    def __str__(self):
        return f"User ID: {self.user_id}, Username: {self.username}"

class Destination:
    def __init__(self, name, location):
        self.destination_id = self.get_next_destination_id()
        self.name = name
        self.location = location

    @staticmethod
    def get_next_destination_id():
        try:
            with open("destination_id.txt", "r") as file:
                destination_id = int(file.read())
        except FileNotFoundError:
            destination_id = 1
        with open("destination_id.txt", "w") as file:
            file.write(str(destination_id + 1))
        return destination_id

    def __str__(self):
        return f"Destination ID: {self.destination_id}, Name: {self.name}"

class Room:
    next_room_id = 1

    def __init__(self, status, check_in, check_out, no_of_beds):
        self.room_id = Room.next_room_id
        Room.next_room_id += 1
        self.status = status
        self.check_in = check_in
        self.check_out = check_out
        self.no_of_beds = no_of_beds

    def __str__(self):
        return f"Room ID: {self.room_id}, Status: {self.status}, Beds: {self.no_of_beds}, Check-in: {self.check_in}, Check-out: {self.check_out}"

class Accommodation:
    next_accommodation_id = 1

    def __init__(self, name, address):
        self.accommodation_id = Accommodation.next_accommodation_id
        Accommodation.next_accommodation_id += 1
        self.name = name
        self.address = address
        self.rooms = []

    def add_room(self, status, check_in, check_out, no_of_beds):
        room = Room(status, check_in, check_out, no_of_beds)
        self.rooms.append(room)
        return room

    def __str__(self):
        return f"Accommodation ID: {self.accommodation_id}, Name: {self.name}, Address: {self.address}"

class Trip:
    def __init__(self, user, destination, accommodation, start_date, end_date):
        self.trip_id = destination.destination_id
        self.user = user
        self.destination = destination
        self.accommodation = accommodation
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Trip ID: {self.trip_id}, Destination: {self.destination.name}, Start Date: {self.start_date}, End Date: {self.end_date}, Accommodation: {self.accommodation.name}"

# Get user input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Create user object
user1 = User(username, password)

# Get destination details
destination_name = input("Enter the name for Destination: ")
destination_location = input("Enter the location for Destination: ")

# Create destination object
destination = Destination(destination_name, destination_location)

# Get room details
room_status = input("Enter room status: ")
room_check_in = input("Enter room check-in date (DD-MM-YYYY): ")
room_check_out = input("Enter room check-out date (DD-MM-YYYY): ")
room_beds = int(input("Enter number of beds in the room: "))

# Create room object
room = Room(room_status, room_check_in, room_check_out, room_beds)

# Get accommodation details
accommodation_name = input("Enter accommodation name: ")
accommodation_address = input("Enter accommodation address: ")

# Create accommodation object
accommodation = Accommodation(accommodation_name, accommodation_address)
accommodation.add_room(room.status, room.check_in, room.check_out, room.no_of_beds)  # Add room to accommodation

# Plan a trip to the destination
trip_start_date = input("Enter the start date for the trip (DD-MM-YYYY): ")
trip_end_date = input("Enter the end date for the trip (DD-MM-YYYY): ")

# Create trip object
trip = Trip(user1, destination, accommodation, trip_start_date, trip_end_date)

# Add the trip object to the user's trips list
user1.trips.append(trip)

# Display user and trip information
print(f"\n{user1}")
print(f"{destination}\n")
print(f"Accommodation Information:")
print(accommodation)
print(f"Trip Information:")
print(trip)
