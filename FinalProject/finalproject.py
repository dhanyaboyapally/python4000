import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Loads the dataset and processes date format"""
    try:
        df = pd.read_csv(file_path)
        df['Week'] = pd.to_datetime(df['week']).dt.date  # Convert date format
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        return None

def list_dates(df):
    """Prints unique dates from the dataset"""
    dates = sorted(df['Week'].unique())
    print("\nDates with recorded learning modalities:")
    for date in dates:
        print(date)

def learning_modality_by_state(df, state_code, date):
    """Displays learning modality breakdown for a given state and date"""
    filtered_df = df[(df['state'] == state_code) & (df['Week'] == date)]
    if filtered_df.empty:
        print("\nNo data found for the given state and date.")
        return

    total_schools = filtered_df['operational_schools'].sum()
    modality_counts = filtered_df['learning_modality'].value_counts()
    modality_percentages = modality_counts / total_schools * 100

    print(f"\nDate: {date}")
    print(f"State: {state_code}")
    print(f"Total schools: {total_schools}")
    
    for modality, count in modality_counts.items():
        percentage = modality_percentages.get(modality, 0)
        print(f"{count} ({percentage:.1f}%) {modality}")

def plot_trends(df, state_code):
    """Plots trends of learning modalities in a given state over time"""
    filtered_df = df[df['state'] == state_code]
    if filtered_df.empty:
        print("\nNo data found for the given state.")
        return
    
    grouped = filtered_df.groupby(['Week', 'learning_modality']).size().unstack(fill_value=0)
    grouped.plot(kind='line', marker='o', figsize=(10, 5))

    plt.title(f'Learning Modality Trends for {state_code}')
    plt.xlabel('Date')
    plt.ylabel('Number of Schools')
    plt.legend(title="Modality")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def main():
    file_path = input("Data file path : ")
    df = load_data(file_path)
    if df is None:
        return

    while True:
        print("\nData analysis options:")
        print("1. List dates")
        print("2. Learning modality by state on date")
        print("3. Plot trends over time for a state")
        print("4. Exit")

        choice = input("Enter the number of the option (1, 2, 3, or 4): ")
        
        if choice == "1":
            list_dates(df)
        elif choice == "2":
            state_code = input("Enter the two-letter state code: ").upper()
            date = input("Enter the date (MM/DD/YYYY): ")
            learning_modality_by_state(df, state_code, date)
        elif choice == "3":
            state_code = input("Enter the two-letter state code: ").upper()
            plot_trends(df, state_code)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
