# Generated by Django 2.1.7 on 2019-03-25 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='id',
        ),
        migrations.AddField(
            model_name='application',
            name='stu_apps',
            field=models.TextField(default=1, max_length=2048),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.student_acc'),
        ),
    ]