# Generated by Django 4.2.2 on 2023-08-10 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0003_alter_answer_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='downvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='upvotes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]