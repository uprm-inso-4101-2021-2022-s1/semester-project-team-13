# Generated by Django 3.2.7 on 2021-09-30 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beach', '0004_auto_20210930_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='beach',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beach.beach'),
        ),
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default_user_pic.jpg', upload_to='profile_pic'),
        ),
    ]
