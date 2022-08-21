import csv

from reviews.models import Category


def run():
    with open('static/data/category.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Category.objects.all().delete()

        for row in reader:
            print(row)

            category = Category(
                id=row[0],
                name=row[1],
                slug=row[2]
            )
            category.save()
