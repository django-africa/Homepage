# Generated by Django 3.0.3 on 2020-02-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=120)),
                ('message', models.TextField()),
                ('submited_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
