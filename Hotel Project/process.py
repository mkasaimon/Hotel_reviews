from datetime import datetime


def get_total_reviews(reviews):
    return len(reviews)


def get_reviews_by_hotel(reviews, hotel_name):
    filtered_reviews = [review for review in reviews if review[1].lower() == hotel_name.lower()]
    return filtered_reviews


def get_reviews_by_dates(reviews, start_date, end_date):
    filtered_reviews = []
    for review in reviews:
        review_date = datetime.strptime(review[0], '%m/%d/%Y').date()
        if start_date <= review_date <= end_date:
            filtered_reviews.append(review)
    return filtered_reviews


def group_reviews_by_nationality(reviews):
    grouped_reviews = {}
    for review in reviews:
        nationality = review[4]
        if nationality in grouped_reviews:
            grouped_reviews[nationality].append(review)
        else:
            grouped_reviews[nationality] = [review]
    return grouped_reviews


def get_reviews_summary(reviews):
    summary = {}
    for review in reviews:
        date = review[0]
        sentiment = review[2]
        rating = float(review[5])

        if date in summary:
            if sentiment == 'Positive':
                summary[date]['Total Positive Reviews'] += 1
            else:
                summary[date]['Total Negative Reviews'] += 1
            summary[date]['Ratings'].append(rating)
        else:
            summary[date] = {
                'Total Positive Reviews': 1 if sentiment == 'Positive' else 0,
                'Total Negative Reviews': 1 if sentiment == 'Negative' else 0,
                'Ratings': [rating]
            }

    # Calculate average rating for each date
    for date, data in summary.items():
        ratings = data['Ratings']
        average_rating = sum(ratings) / len(ratings)
        data['Average Rating'] = average_rating
        del data['Ratings']

    return summary
