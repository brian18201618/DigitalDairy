# Generated by Django 2.2 on 2019-08-29 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitaldairy', '0006_auto_20190828_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyfeeding',
            name='feeding_category',
            field=models.CharField(choices=[('Milker', 'Milker'), ('Heifer', 'Heifer'), ('Dry', 'Dry'), ('Steamer', 'Steamer'), ('Incalf Heifer', 'Incalf Heifer'), ('Calf', 'Calf'), ('Weaner', 'Weaner'), ('Weaner 1', 'Weaner 1'), ('Weaner 2', 'Weaner 2'), ('Weaner 3', 'Weaner 3'), ('Yearling', 'Yearling'), ('Bulling', 'Bulling'), ('Bull', 'Bull')], max_length=30),
        ),
        migrations.AlterField(
            model_name='feedingprogramme',
            name='feeding_category',
            field=models.CharField(choices=[('Milker', 'Milker'), ('Heifer', 'Heifer'), ('Dry', 'Dry'), ('Steamer', 'Steamer'), ('Incalf Heifer', 'Incalf Heifer'), ('Calf', 'Calf'), ('Weaner', 'Weaner'), ('Weaner 1', 'Weaner 1'), ('Weaner 2', 'Weaner 2'), ('Weaner 3', 'Weaner 3'), ('Yearling', 'Yearling'), ('Bulling', 'Bulling'), ('Bull', 'Bull')], max_length=30),
        ),
    ]
