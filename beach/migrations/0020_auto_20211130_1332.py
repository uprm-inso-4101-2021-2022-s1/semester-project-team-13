# Generated by Django 3.2.7 on 2021-11-30 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beach', '0019_profile_bucketlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='beach',
            name='boatRating',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='beach',
            name='diveRating',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='beach',
            name='isCleanRating',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='beach',
            name='lifeguardRating',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='beach',
            name='loungeRating',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='beach',
            name='overallRating',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='beach',
            name='safetyRating',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='beach',
            name='surfRating',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='beach',
            name='swimRating',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rating',
            name='beach',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beach.beach'),
        ),
    ]