import csv

from reviews.models import Review


def run():
    with open('static/data/review.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Review.objects.all().delete()

        for row in reader:
            print(row)

            review = Review(
                id=row[0],
                title_id=row[1],
                text=row[2],
                author_id=row[3],
                score=row[4],
                pub_date=row[5],
            )
            review.save()
