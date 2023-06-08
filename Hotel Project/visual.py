import matplotlib.pyplot as plt


def display_reviews_by_nationality(reviews_by_nationality):
    # Sort the reviews by nationality based on the number of reviews
    sorted_reviews = sorted(reviews_by_nationality.items(), key=lambda x: x[1], reverse=True)

    # Select the top 15 nationalities
    top_nationalities = dict(sorted_reviews[:15])

    # Add the count of "Other" nationalities
    other_count = sum(value for _, value in sorted_reviews[15:])
    if other_count > 0:
        top_nationalities["Other"] = other_count

    # Prepare the data for visualization
    nationalities = list(top_nationalities.keys())
    review_counts = list(top_nationalities.values())

    # Plotting the bar chart
    plt.barh(nationalities, review_counts)
    plt.xlabel("Review Count")
    plt.ylabel("Nationality")
    plt.title("Number of Reviews per Nationality")
    plt.show()


def display_animated_visualization(reviews_data):
    positive_reviews = []
    negative_reviews = []
    average_ratings = []

    # Process the reviews data to extract required information
    for review in reviews_data:
        positive_count = 0
        negative_count = 0
        total_rating = 0

        for review_data in review:
            if review_data == "positive":
                positive_count += 1
            elif review_data == "negative":
                negative_count += 1
            elif isinstance(review_data, float):
                total_rating += review_data

        positive_reviews.append(positive_count)
        negative_reviews.append(negative_count)
        average_ratings.append(total_rating / (positive_count + negative_count))

    # Prepare the data for visualization
    dates = range(1, len(reviews_data) + 1)

    # Plotting the animated line chart
    plt.plot(dates, positive_reviews, label="Positive Reviews")
    plt.plot(dates, negative_reviews, label="Negative Reviews")
    plt.plot(dates, average_ratings, label="Average Rating")
    plt.xlabel("Date")
    plt.ylabel("Count / Rating")
    plt.title("Reviews and Average Rating Over Time")
    plt.legend()
    plt.show()


def display_pie_chart(reviews, hotel_name):
    # Filter reviews for the specified hotel name
    hotel_reviews = [review for review in reviews if review[1] == hotel_name]

    positive_count = sum(review[2] == "Positive" for review in hotel_reviews)
    negative_count = sum(review[2] == "Negative" for review in hotel_reviews)

    # Check if there are no reviews for the hotel
    if positive_count == 0 and negative_count == 0:
        print("No reviews found for the specified hotel.")
        return

    labels = ["Positive", "Negative"]
    counts = [positive_count, negative_count]
    colors = ["green", "red"]

    plt.pie(counts, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    plt.axis("equal")
    plt.title(f"Positive vs Negative Reviews for {hotel_name}")
    plt.show()

