import math

def get_square_footage(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be positive. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_price_per_box(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be positive. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_labor_rate(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value must be non-negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        print("\n=== Flooring Estimator ===\n")
        # Get room dimensions
        square_footage = get_square_footage("Enter the square footage of the room (feet): ")
        # square_footage = length * width

        # Get tile and labor costs
        price_per_box = get_price_per_box("Enter the price per box of tiles: $")
        labor_rate = get_labor_rate("Enter the labor rate per hour: $")

        # Calculate required boxes and hours
        boxes = math.ceil(square_footage / 25)
        hours = (square_footage / 50) * 1.5
        hours_rounded = round(hours, 1)

        # Calculate costs
        tiles_cost = boxes * price_per_box
        labor_charges = hours * labor_rate
        total_cost = tiles_cost + labor_charges

        # Display results
        print("\nEstimation Results:")
        print(f"Boxes of tiles required: {boxes}")
        print(f"Hours of labor required: {hours_rounded:.1f}")
        print(f"Cost of tiles: ${tiles_cost:.2f}")
        print(f"Labor charges: ${labor_charges:.2f}")
        print(f"Total cost: ${total_cost:.2f}")

        # Prompt for another estimate
        while True:
            repeat = input("\nWould you like to perform another estimate? (y/n): ").strip().lower()
            if repeat == 'y':
                break
            elif repeat == 'n':
                print("\nThank you for using the Flooring Estimator. Goodbye!")
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
