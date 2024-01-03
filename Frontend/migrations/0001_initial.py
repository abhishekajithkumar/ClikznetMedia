# Generated by Django 4.2.4 on 2023-10-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Username', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=70, null=True)),
                ('Password', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]