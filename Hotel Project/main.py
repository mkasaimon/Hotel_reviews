import tui
import process
import visual


def run():
    reviews_data = []  # Initialize an empty list to store the data

    tui.welcome()  # Display the welcome message

    # Load the data
    tui.display_data_loading_message()
    try:
        reviews_data = tui.load_data()
        tui.display_data_loading_complete_message(len(reviews_data))
    except FileNotFoundError:
        tui.display_data_loading_error_message()

    while True:
        main_menu_option = tui.display_main_menu()  # Display the main menu and get the user's option

        if main_menu_option == 1:  # Processing data
            tui.display_data_processing_message()

            sub_menu_option = tui.display_processing_submenu()  # Display the processing submenu

            if sub_menu_option == 1:  # Retrieve reviews by hotel name
                tui.display_review_retrieval_message()
                hotel_name = tui.get_hotel_name()
                reviews = process.get_reviews_by_hotel(reviews_data, hotel_name)
                tui.display_reviews(reviews)
                tui.display_review_retrieval_complete_message()

            elif sub_menu_option == 2:  # Retrieve reviews by review dates
                tui.display_reviews_retrieval_message()
                start_date, end_date = tui.get_review_dates()
                reviews = process.get_reviews_by_dates(reviews_data, start_date, end_date)
                tui.display_reviews(reviews)
                tui.display_reviews_retrieval_complete_message()

            elif sub_menu_option == 3:  # Group reviews by nationality
                tui.display_grouping_message()
                reviews_grouped = process.group_reviews_by_nationality(reviews_data)
                tui.display_reviews_grouped(reviews_grouped)
                tui.display_grouping_complete_message()

            elif sub_menu_option == 4:  # Summarize the reviews
                tui.display_summary_message()
                reviews_summary = process.get_reviews_summary(reviews_data)
                tui.display_reviews_summary(reviews_summary)
                tui.display_summary_complete_message()

            tui.display_data_processing_complete_message()

        elif main_menu_option == 2:  # Visualizing data
            tui.display_data_visualization_message()

            visualization_option = tui.get_visualization_option()
            if visualization_option == 1:  # Pie chart of positive and negative reviews for a hotel
                tui.display_hotel_selection_message()
                hotel_name = tui.get_hotel_name()
                visual.display_pie_chart(reviews_data, hotel_name)

            elif visualization_option == 2:  # Number of reviews per nationality
                reviews_by_nationality = process.group_reviews_by_nationality(reviews_data)
                visual.display_reviews_by_nationality(reviews_by_nationality)

            elif visualization_option == 3:  # Animated visualization of reviews over time
                visual.display_animated_visualization(reviews_data)

            tui.display_data_visualization_complete_message()

        elif main_menu_option == 3:  # Exporting reviews
            tui.display_export_message()

            export_option = tui.get_export_option()
            if export_option == 1:  # Export all reviews
                tui.display_export_all_reviews_message()
                tui.export_reviews(reviews_data)

            elif export_option == 2:  # Export reviews for a specific nationality
                tui.display_export_by_nationality_message()
                nationality = tui.get_nationality()
                reviews_filtered = [review for review in reviews_data if review[2] == nationality]
                tui.export_reviews(reviews_filtered)

            tui.display_export_complete_message()

        elif main_menu_option == 4:  # Exiting the program1

            break

        else:  # Invalid option
            tui.display_error_message()


if __name__ == "__main__":
    run()
