# Generated by Django 3.2.7 on 2021-09-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0007_auto_20180914_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='null_field',
            field=models.BooleanField(default=None, null=True),
        ),
    ]