import csv

from users.models import User


def run():
    with open('static/data/users.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        User.objects.all().delete()

        for row in reader:
            print(row)

            user = User(
                id=row[0],
                username=row[1],
                email=row[2],
                role=row[3],
                bio=row[4],
                first_name=row[5],
                last_name=row[6],
            )
            user.save()
