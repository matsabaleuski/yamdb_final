import csv

from reviews.models import Title


def run():
    with open('static/data/titles.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Title.objects.all().delete()

        for row in reader:
            print(row)

            title = Title(
                id=row[0],
                name=row[1],
                year=row[2],
                category_id=row[3]
            )
            title.save()
