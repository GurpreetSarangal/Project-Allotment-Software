# Generated by Django 4.0.2 on 2022-03-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_alter_guide_mobile_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='mobile_2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
