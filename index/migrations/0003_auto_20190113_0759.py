# Generated by Django 2.1 on 2019-01-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.AlterField(
            model_name='events',
            name='Image',
            field=models.ImageField(upload_to='events'),
        ),
    ]
