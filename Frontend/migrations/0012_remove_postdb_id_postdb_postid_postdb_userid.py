# Generated by Django 4.2.4 on 2023-11-08 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0011_remove_registerdb_id_registerdb_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postdb',
            name='id',
        ),
        migrations.AddField(
            model_name='postdb',
            name='PostId',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postdb',
            name='UserId',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
