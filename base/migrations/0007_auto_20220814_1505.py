# Generated by Django 3.1.14 on 2022-08-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20220814_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.IntegerField(choices=[(1, 'Tops'), (2, 'Bottoms'), (3, 'Otro')], max_length=200),
        ),
    ]