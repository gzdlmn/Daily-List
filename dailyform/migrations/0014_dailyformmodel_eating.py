# Generated by Django 3.2 on 2021-04-10 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyform', '0013_auto_20210410_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyformmodel',
            name='eating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=3, null=True),
        ),
    ]