# Generated by Django 5.0 on 2024-04-08 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
