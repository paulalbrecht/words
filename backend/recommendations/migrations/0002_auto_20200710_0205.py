# Generated by Django 3.0.8 on 2020-07-10 02:05
# Load initial tab based dataset

from django.db import migrations
from django.db import transaction
from django.db import IntegrityError
import csv


DATA_FILE = '../full-stack-coding-exercise-data.txt'

def load_recommendations(apps, schema_editor):
    Recommendation = apps.get_model('recommendations', 'Recommendation')

    with open(DATA_FILE) as books:
        book_reader = csv.reader(books, delimiter='\t')
        book_list = list(book_reader)[1:]
        for title, author, recommender, source, amazon_link, description, rec_type, genre, length, publish_year, on_list, review_excerpt in book_list:
            try:
                with transaction.atomic():
                    Recommendation.objects.create(title=title,
                               author=author,
                               recommender=recommender,
                               source=source,
                               amazon_link=amazon_link,
                               description=description,
                               rec_type=rec_type,
                               genre=genre,
                               length=length,
                               publish_year=publish_year,
                               on_list=on_list,
                               review_excerpt=review_excerpt)
            except IntegrityError:
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_recommendations),
    ]