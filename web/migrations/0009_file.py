# Generated by Django 2.0.6 on 2018-07-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20180725_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=30)),
                ('uploadFile', models.FileField(upload_to='disk/upload/')),
            ],
        ),
    ]
