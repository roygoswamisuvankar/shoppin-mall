# Generated by Django 3.2.9 on 2022-01-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0002_rename_admin_admin2'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('dept', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=30)),
                ('basicsal', models.CharField(max_length=20)),
            ],
        ),
    ]
