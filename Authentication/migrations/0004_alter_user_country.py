# Generated by Django 5.0.4 on 2024-04-08 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_remove_club_staff_profile_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]
