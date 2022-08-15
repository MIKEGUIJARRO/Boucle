# Generated by Django 3.1.14 on 2022-08-14 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20220814_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='drop_off_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='cloth',
            name='pick_up_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='cloth',
            name='pick_up_hour',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='stage',
            field=models.ForeignKey(default='stage-1', null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.stage'),
        ),
    ]
