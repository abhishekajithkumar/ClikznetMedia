# Generated by Django 4.2.4 on 2023-11-23 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0022_followerdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followerdb',
            name='FollowerId',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='followerdb',
            name='FollowingId',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
