# Generated by Django 4.1.7 on 2023-02-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ddd', upload_to='pics'),
            preserve_default=False,
        ),
    ]
