class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.trips = []  # List to store user's trips

    def __str__(self):
        return f"User ID: {self.user_id}, Username: {self.username}"

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
        self.is_booked = False  # Status of accommodation booking

    def __str__(self):
        return f"Accommodation ID: {self.accommodation_id}, Name: {self.name}, Address: {self.address}"

class Budget:
    def __init__(self):
        self.total_budget = 0
        self.expenses = {}  # Dictionary to store expenses by category

        # Example categories for expenses
        self.expense_categories = ["Accommodation", "Food", "Transportation"]

        # Initialize expenses for each category to 0
        for category in self.expense_categories:
            self.expenses[category] = 0

    def __str__(self):
        return f"Total Budget: {self.total_budget}"

# Get user input
username = input("Enter your username: ")
destination_name = input("Enter the destination name: ")
start_date = input("Enter the trip start date (DD-MM-YYYY): ")
end_date = input("Enter the trip end date (DD-MM-YYYY): ")

# Create user, destination, and trip objects with unique IDs
user1 = User(1, username, "password123")
destination1 = Destination(1, destination_name, "France")
trip1 = Trip(1, user1, destination1, start_date, end_date)

# Display user, trip, and destination information along with their IDs
print(user1)
print(trip1)
print(destination1)