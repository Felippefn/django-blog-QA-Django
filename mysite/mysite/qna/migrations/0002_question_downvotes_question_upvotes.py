# Generated by Django 4.2.4 on 2023-08-03 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='downvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='upvotes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
