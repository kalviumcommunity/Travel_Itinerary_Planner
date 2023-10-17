# Define the User class
class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.trips = []  

    def __str__(self):
        return f"User ID: {self.user_id}, Username: {self.username}"
    
    # Define the Budget class
class Budget:
    def __init__(self):
        self.total_budget = 0
        self.expenses = {}  

        self.expense_categories = ["Accommodation", "Food", "Transportation"]

        for category in self.expense_categories:
            self.expenses[category] = 0

    def __str__(self):
        return f"Total Budget: {self.total_budget}"

# Define the Destination class
class Destination:
    def __init__(self, destination_id, name, location):
        self.destination_id = destination_id  
        self.name = name 
        self.location = location  

    def __str__(self):
        return f"Destination ID: {self.destination_id}, Name: {self.name}"  
      
# Define the Trip class
class Trip:
    def __init__(self, trip_id, user, destination, start_date, end_date):
        self.trip_id = trip_id
        self.user = user
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.accommodations = [] 
        self.budget = Budget()  

    def __str__(self):
        return f"Trip ID: {self.trip_id}, Destination: {self.destination.name}, Start Date: {self.start_date}, End Date: {self.end_date}"

class Destination:
    def __init__(self, destination_id, name, location):
        self.destination_id = destination_id
        self.name = name
        self.location = location

    def __str__(self):
        return f"Destination ID: {self.destination_id}, Name: {self.name}"

class Accommodation:
    def __init__(self, accommodation_id, name, address, check_in, check_out):
        self.accommodation_id = accommodation_id
        self.name = name
        self.address = address
        self.check_in = check_in
        self.check_out = check_out
        self.is_booked = False  

    def __str__(self):
        return f"Accommodation ID: {self.accommodation_id}, Name: {self.name}, Address: {self.address}"

class Budget:
    def __init__(self):
        self.total_budget = 0
        self.expenses = {}  

        self.expense_categories = ["Accommodation", "Food", "Transportation"]

        for category in self.expense_categories:
            self.expenses[category] = 0

    def __str__(self):
        return f"Total Budget: {self.total_budget}"

username = input("Enter your username: ")


user1 = User(1, username, "password123")
destination1 = Destination(1, destination_name, "France")
trip1 = Trip(1, user1, destination1, start_date, end_date)

print(user1)
print(trip1)
print(destination1)

# Create an array of Destination objects
destinations = []
num_destinations = int(input("Enter the number of destinations you want to add: "))

# Add destinations to the array
for i in range(num_destinations):
    destination_name = input(f"Enter the name for Destination {i+1}: ")
    location = input(f"Enter the location for Destination {i+1}: ")
    destination = Destination(i + 1, destination_name, location)
    destinations.append(destination)

# Set the number of trips to 1
num_trips = 1

# Add a trip to the array
for i in range(num_trips):
    destination_id = int(input("Enter the destination ID for the trip: "))
    start_date = input("Enter the start date for the trip (DD-MM-YYYY): ")
    end_date = input("Enter the end date for the trip (DD-MM-YYYY): ")

    # Assuming destination_id is always valid
    selected_destination = destinations[destination_id - 1]

    trip = Trip(i + 1, user1, selected_destination, start_date, end_date)
    user1.trips.append(trip)  # Add the trip object to the user's trips list
    print(f"Trip to {selected_destination.name} from {start_date} to {end_date} added successfully.")

# Display user and trip information
print(f"User Information: {user1}")
print("Trips:")
for trip in user1.trips:
    print(trip)
