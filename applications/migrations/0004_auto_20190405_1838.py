# Generated by Django 2.1.7 on 2019-04-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20190405_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_id',
            field=models.IntegerField(default=0, max_length=10, primary_key=True, serialize=False),
        ),
    ]