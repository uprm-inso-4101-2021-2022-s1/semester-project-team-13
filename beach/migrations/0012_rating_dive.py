# Generated by Django 3.2.7 on 2021-10-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beach', '0011_auto_20211004_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='dive',
            field=models.PositiveIntegerField(null=True),
        ),
    ]