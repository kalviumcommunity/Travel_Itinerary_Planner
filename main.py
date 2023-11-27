class BaseEntity:
    def __init__(self, name, id_file):
        self._id = self._get_next_id(id_file)
        self._name = name

    def _get_next_id(self, id_file):
        try:
            with open(id_file, "r") as file:
                entity_id = int(file.read())
        except FileNotFoundError:
            entity_id = 1

        with open(id_file, "w") as file:
            file.write(str(entity_id + 1))

        return entity_id

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def __str__(self):
        return f"{self.__class__.__name__} ID: {self._id}, Name: {self._name}"


class User(BaseEntity):
    def __init__(self, username, password):
        super().__init__(username, "user_id.txt")
        self._username = username
        self._password = password
        self._trips = []

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_trips(self):
        return self._trips

    def __str__(self):
        return f"{super().__str__()}, Username: {self._username}"


class Destination(BaseEntity):
    def __init__(self, name, location):
        super().__init__(name, "destination_id.txt")
        self._location = location

    def get_location(self):
        return self._location

    def __str__(self):
        return f"{super().__str__()}, Location: {self._location}"


class Room(BaseEntity):
    next_room_id = 1

    def __init__(self, no_of_beds):
        super().__init__(f"Room-{Room.next_room_id}", "room_id.txt")
        Room.next_room_id += 1
        self._no_of_beds = no_of_beds

    def get_no_of_beds(self):
        return self._no_of_beds

    def __str__(self):
        return f"{super().__str__()}, Beds: {self._no_of_beds}"


class Accommodation(BaseEntity):
    next_accommodation_id = 1

    def __init__(self, name, address):
        super().__init__(name, "accommodation_id.txt")
        self._address = address
        self._rooms = []

    def add_room(self, no_of_beds):
        room = Room(no_of_beds)
        self._rooms.append(room)
        return room

    def get_address(self):
        return self._address

    def get_rooms(self):
        return self._rooms

    def __str__(self):
        return f"{super().__str__()}, Address: {self._address}, Rooms: {len(self._rooms)}"

class Trip(BaseEntity):
    def __init__(self, user, destination, accommodation, start_date, end_date):
        super().__init__(destination.get_name(), "trip_id.txt")
        self._user = user
        self._destination = destination
        self._accommodation = accommodation
        self._start_date = start_date
        self._end_date = end_date

    def get_user(self):
        """Getter method for the user."""
        return self._user

    def get_destination(self):
        """Getter method for the destination."""
        return self._destination

    def get_accommodation(self):
        """Getter method for the accommodation."""
        return self._accommodation

    def get_start_date(self):
        """Getter method for the start date."""
        return self._start_date

    def get_end_date(self):
        """Getter method for the end date."""
        return self._end_date

    def __str__(self):
        return f"{super().__str__()}, User: {self._user.get_name()}, Destination: {self._destination.get_name()}, Accommodation: {self._accommodation.get_name()}, Start Date: {self._start_date}, End Date: {self._end_date}"


# Example Usage:

# Create User
user = User("JohnDoe", "password123")

# Create Destination
destination = Destination("Paris", "France")

# Create Room
room = Room(2)

# Create Accommodation
accommodation = Accommodation("Hotel XYZ", "123 Main St")
accommodation.add_room(room.get_no_of_beds())

# Create Trip
trip = Trip(user, destination, accommodation, "2023-11-01", "2023-11-07")

# Print information
print(user)
print(destination)
print(room)
print(accommodation)
print(trip)

