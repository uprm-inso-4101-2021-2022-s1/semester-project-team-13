# Generated by Django 3.2.7 on 2021-10-27 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beach', '0016_auto_20211027_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default_user_pic.jpg', upload_to='media/profile_pic'),
        ),
    ]
