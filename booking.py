import random

# Predefined cab rates (Rs per km)
CAB_TYPES = {
    "1": ("Auto", 12),
    "2": ("Sedan", 18),
    "3": ("SUV", 25),
}

# Predefined routes: (source, destination, distance in km)
ROUTES = {
    "1": ("Pune Station", "Shivajinagar", 5),
    "2": ("Swargate", "Kothrud", 8),
    "3": ("Hinjawadi", "Wakad", 10),
}


def choose_cab():
    print("\nChoose your cab type:")
    print("1. Auto   (Rs 12/km)")
    print("2. Sedan  (Rs 18/km)")
    print("3. SUV    (Rs 25/km)")
    choice = input("Enter cab choice (1-3): ").strip()
    if choice in CAB_TYPES:
        return CAB_TYPES[choice]
    print("Invalid cab choice! Returning to main menu.")
    return None


def choose_route():
    print("\nAvailable routes:")
    for number, (source, destination, distance) in ROUTES.items():
        print(f"{number}. {source} -> {destination} ({distance} km)")
    choice = input("Enter route number (1-3): ").strip()
    if choice in ROUTES:
        return ROUTES[choice]
    print("Invalid route choice! Returning to main menu.")
    return None


def book_ride():
    cab = choose_cab()
    if cab is None:
        return
    cab_name, rate = cab

    route = choose_route()
    if route is None:
        return
    source, destination, distance = route

    fare = rate * distance

    print("\n------ Ride Summary ------")
    print(f"Cab Type    : {cab_name}")
    print(f"Source      : {source}")
    print(f"Destination : {destination}")
    print(f"Distance    : {distance} km")
    print(f"Rate        : Rs {rate}/km")
    print(f"Total Fare  : Rs {fare}  ({distance} x {rate})")
    print("--------------------------")

    # Cancellation is allowed only BEFORE the OTP is shared
    while True:
        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")
        choice = input("Enter your choice (1-2): ").strip()

        if choice == "1":
            otp = random.randint(1000, 9999)
            print(f"\nYour OTP is: {otp} (shared with you)")
            print("NOTE: OTP has been shared. The ride can NO LONGER be cancelled.")
            print("Booking confirmed! Your cab is on the way.")
            return
        elif choice == "2":
            print("\nRide cancelled. No OTP was shared. Returning to main menu.")
            return
        else:
            print("Invalid choice! Please enter 1 or 2.")


def main():
    print("=== Welcome to the Cab Booking Chatbot ===")
    while True:
        print("\n----- Main Menu -----")
        print("1. Book Ride")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ").strip()

        if choice == "1":
            book_ride()
        elif choice == "2":
            print("Thank you for using Cab Booking Chatbot. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")


main()