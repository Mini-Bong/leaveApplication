# Generated by Django 2.1.7 on 2019-03-24 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190320_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hod_acc',
            name='branch_name',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='hod_acc',
            name='email',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hod_acc',
            name='hod_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='hod_acc',
            name='mobile_no',
            field=models.IntegerField(null=True),
        ),
    ]
