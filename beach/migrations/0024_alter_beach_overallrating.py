# Generated by Django 3.2.7 on 2021-11-30 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beach', '0023_alter_beach_overallrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beach',
            name='overallRating',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
    ]
