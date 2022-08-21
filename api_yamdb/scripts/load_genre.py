import csv

from reviews.models import Genre


def run():
    with open('static/data/genre.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Genre.objects.all().delete()

        for row in reader:
            print(row)

            genre = Genre(
                id=row[0],
                name=row[1],
                slug=row[2]
            )
            genre.save()
