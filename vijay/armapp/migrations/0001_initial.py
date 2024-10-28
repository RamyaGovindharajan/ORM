# Generated by Django 5.1.2 on 2024-10-26 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankloan',
            fields=[
                ('Name', models.CharField(max_length=30)),
                ('Account_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Loan_amount', models.IntegerField()),
                ('Interest_amount', models.FloatField()),
                ('DOB', models.DateField()),
            ],
        ),
    ]