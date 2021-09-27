# Generated by Django 3.2 on 2021-04-06 22:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dailyform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyformmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dailyformmodel',
            name='sleeping',
            field=models.CharField(choices=[('1', ''), ('2', ''), ('3', '')], max_length=3, null=True),
        ),
    ]