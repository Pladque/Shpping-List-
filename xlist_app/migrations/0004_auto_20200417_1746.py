# Generated by Django 3.0.5 on 2020-04-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xlist_app', '0003_auto_20200417_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingitem',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
