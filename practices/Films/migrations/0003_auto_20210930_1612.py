# Generated by Django 3.2.7 on 2021-09-30 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Films', '0002_remove_extenduser_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extenduser',
            name='gender',
        ),
        migrations.AddField(
            model_name='moviesname',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50),
        ),
        migrations.AlterField(
            model_name='extenduser',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='extenduser',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
