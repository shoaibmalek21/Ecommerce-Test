# Generated by Django 3.1.1 on 2020-11-08 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SELLER_ID', models.IntegerField()),
                ('first_name', models.CharField(help_text='Optional.', max_length=30)),
                ('last_name', models.CharField(help_text='Optional.', max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('contact', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
