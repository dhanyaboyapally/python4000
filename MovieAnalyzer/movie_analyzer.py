import csv
import os

class MovieAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.movies = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.movies = list(reader)
                for movie in self.movies:
                    movie["Year"] = int(movie["Year"])
                    movie["Rating"] = float(movie["Rating"])
        except Exception as e:
            print(f"Error loading data: {e}")

    def display_summary_statistics(self):
        if not self.movies:
            print("No data available.")
            return

        total_rating = sum(movie["Rating"] for movie in self.movies)
        average_rating = total_rating / len(self.movies)
        highest_rated_movies = [movie for movie in self.movies if movie["Rating"] == max(movie["Rating"] for movie in self.movies)]
        lowest_rated_movies = [movie for movie in self.movies if movie["Rating"] == min(movie["Rating"] for movie in self.movies)]

        print(f"Number of movies: {len(self.movies)}")
        print(f"Average rating: {average_rating:.2f}")
        print("Highest rated movie(s):")
        for movie in highest_rated_movies:
            print(f"  - {movie['Title']} ({movie['Year']}) with rating {movie['Rating']}")
        print("Lowest rated movie(s):")
        for movie in lowest_rated_movies:
            print(f"  - {movie['Title']} ({movie['Year']}) with rating {movie['Rating']}")

    def display_movies_sorted_by_rating(self):
        sorted_movies = sorted(self.movies, key=lambda x: x["Rating"], reverse=True)
        for movie in sorted_movies:
            print(f"{movie['Title']} ({movie['Year']}) - Rating: {movie['Rating']}")

    def display_movies_sorted_by_year(self):
        sorted_movies = sorted(self.movies, key=lambda x: x["Year"])
        for movie in sorted_movies:
            print(f"{movie['Title']} ({movie['Year']}) - Rating: {movie['Rating']}")

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Display summary statistics.")
            print("2. Display movies sorted by rating (descending).")
            print("3. Display movies sorted by year (ascending).")
            print("4. Exit program.")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_summary_statistics()
            elif choice == "2":
                self.display_movies_sorted_by_rating()
            elif choice == "3":
                self.display_movies_sorted_by_year()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    file_path = input("Enter the path for the movie csv data file: ")
    if os.path.exists(file_path):
        analyzer = MovieAnalyzer(file_path)
        analyzer.run()
    else:
        print("File not found. Please check the path and try again.")