# Define the Destination class
class Destination:
    def __init__(self, destination_id, name, location):
        self.destination_id = destination_id
        self.name = name
        self.location = location

    def __str__(self):
        return f"Destination ID: {self.destination_id}, Name: {self.name}"

# Define the User class
class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.trips = []  # List to store user's trips

    def __str__(self):
        return f"User ID: {self.user_id}, Username: {self.username}"

# Define the Trip class
class Trip:
    def __init__(self, trip_id, user, destination, start_date, end_date):
        self.trip_id = trip_id
        self.user = user
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.accommodations = []  # List to store booked accommodations
        self.budget = Budget()  # Initialize a budget for the trip

    def __str__(self):
        return f"Trip ID: {self.trip_id}, Destination: {self.destination.name}, Start Date: {self.start_date}, End Date: {self.end_date}"

# Get user input
username = input("Enter your username: ")

# Create user object
user1 = User(1, username, "password123")

# Create an array of Destination objects
destinations = []
num_destinations = int(input("Enter the number of destinations you want to add: "))

# Add destinations to the array
for i in range(num_destinations):
    destination_name = input(f"Enter the name for Destination {i+1}: ")
    location = input(f"Enter the location for Destination {i+1}: ")
    destination = Destination(i + 1, destination_name, location)
    destinations.append(destination)

# Create an array of Trip objects
trips = []
num_trips = 1  # Set the number of trips to 1

# Add a trip to the array
for i in range(num_trips):
    destination_id = int(input("Enter the destination ID for the trip: "))
    start_date = input("Enter the start date for the trip (DD-MM-YYYY): ")
    end_date = input("Enter the end date for the trip (DD-MM-YYYY): ")

    # Find the selected destination object from the destinations array
    selected_destination = next((dest for dest in destinations if dest.destination_id == destination_id), None)

    if selected_destination:
        trip = Trip(i + 1, user1, selected_destination, start_date, end_date)
        trips.append(trip)
        print(f"Trip to {selected_destination.name} from {start_date} to {end_date} added successfully.")
        break  # Exit the loop after adding a valid trip
    else:
        print(f"Invalid destination ID {destination_id}. Please try again.")


# Display user, trips, and destinations information
print(user1)
print("Destinations:")
for destination in destinations:
    print(destination)
print("Trips:")
for trip in trips:
    print(trip)
