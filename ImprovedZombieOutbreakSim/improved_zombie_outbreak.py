def get_initial_infected_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Initial infected cannot be negative. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_daily_rate_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Daily infection rate cannot be negative. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_days_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Value must be a positive integer. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

# Main simulation loop
while True:
    print("\n--- Zombie Outbreak Simulation ---")
    initial_infected = get_initial_infected_float("Enter the initial number of infected (Day 0): ")
    daily_rate = get_daily_rate_float("Enter the daily infection rate (in %): ")
    days = get_days_int("Enter the number of days to simulate: ")

    # Calculate the growth factor and total infected
    growth_factor = 1 + (daily_rate / 100)
    total_infected = initial_infected * (growth_factor ** days)
    rounded_total = round(total_infected)

    # Display the result
    print(f"\nAfter {days} days, the total number of infected is approximately {rounded_total}.")

    # Ask the user if they want to perform another simulation
    repeat = input("\nWould you like to perform another simulation? (y/n): ").strip().lower()
    if repeat != 'y':
        print("Exiting the simulation. Goodbye!")
        break
