def welcome():
    print("Welcome to the review analysis program!")


def display_data_loading_message():
    print("Loading data...")


def load_data():
    reviews_data = []
    try:
        with open("data/hotel_reviews.csv", "r") as file:
            next(file)  # Skip the first line (column headers)
            for line in file:
                review = line.strip().split(",")
                reviews_data.append(review)
    except FileNotFoundError:
        reviews_data = []
    return reviews_data


def display_data_loading_complete_message(num_reviews):
    print(f"Data loaded. Total reviews: {num_reviews}")


def display_data_loading_error_message():
    print("Error loading data. File not found.")


def display_main_menu():
    print("Main Menu:")
    print("1. Process Data")
    print("2. Visualize Data")
    print("3. Export Reviews")
    print("4. Exit")
    return int(input("Enter your choice: "))


def display_data_processing_message():
    print("Processing data...")


def display_data_processing_complete_message():
    print("Data processing complete.")


def display_processing_submenu():
    print("Processing Submenu:")
    print("1. Retrieve reviews by hotel name")
    print("2. Retrieve reviews by review dates")
    print("3. Group reviews by nationality")
    print("4. Summarize reviews")
    return int(input("Enter your choice: "))


def get_hotel_name():
    return input("Enter the hotel name: ")


def display_review_retrieval_message():
    print("Retrieving reviews...")


def display_reviews(reviews):
    if not reviews:
        print("No reviews found.")
    else:
        for review in reviews:
            print(review)


def display_review_retrieval_complete_message():
    print("Review retrieval complete.")


def display_reviews_retrieval_message():
    print("Retrieving reviews...")


def get_review_dates():
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    return start_date, end_date


def display_reviews_retrieval_complete_message():
    print("Reviews retrieval complete.")


def display_grouping_message():
    print("Grouping reviews by nationality...")


def display_reviews_grouped(reviews_grouped):
    if not reviews_grouped:
        print("No reviews found.")
    else:
        for nationality, reviews in reviews_grouped.items():
            print(f"Nationality: {nationality}")
            for review in reviews:
                print(review)


def display_grouping_complete_message():
    print("Grouping complete.")


def display_summary_message():
    print("Summarizing reviews...")


def display_reviews_summary(reviews_summary):
    if not reviews_summary:
        print("No reviews found.")
    else:
        for date, summary in reviews_summary.items():
            print(f"Date: {date}")
            print(f"Total negative reviews: {summary['Total Negative Reviews']}")
            print(f"Total positive reviews: {summary['Total Positive Reviews']}")
            print(f"Average rating: {summary['Average Rating']}")


def display_summary_complete_message():
    print("Summary complete.")


def display_data_visualization_message():
    print("Visualizing data...")


def get_visualization_option():
    print("Visualization Options:")
    print("1. Pie chart of positive and negative reviews for a hotel")
    print("2. Number of reviews per nationality")
    print("3. Animated visualization of reviews over time")
    return int(input("Enter your choice: "))


def display_hotel_selection_message():
    print("Please select a hotel:")


def display_data_visualization_complete_message():
    print("Data visualization complete.")


def display_export_message():
    print("Exporting reviews...")


def get_export_option():
    print("Export Options:")
    print("1. Export all reviews")
    print("2. Export reviews for a specific nationality")
    return int(input("Enter your choice: "))


def display_export_all_reviews_message():
    print("Exporting all reviews...")


def display_export_by_nationality_message():
    print("Exporting reviews by nationality...")


def get_nationality():
    return input("Enter the nationality: ")


def display_export_complete_message():
    print("Export complete.")


def export_reviews(reviews):
    if not reviews:
        print("No reviews to export.")
    else:
        filename = input("Enter the filename to save the reviews: ")
        with open(filename, "w") as file:
            for review in reviews:
                file.write(",".join(review) + "\n")
        print("Reviews exported successfully.")


def display_error_message():
    print("Invalid option.")
