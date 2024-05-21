# Generated by Django 5.0.3 on 2024-05-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('age', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=200)),
                ('department', models.CharField(max_length=122)),
                ('address', models.TextField()),
                ('date', models.CharField(max_length=122)),
                ('time', models.CharField(max_length=122)),
                ('doctor', models.CharField(max_length=50)),
                ('slot', models.CharField(max_length=10)),
                ('bmi', models.CharField(max_length=5)),
                ('day', models.CharField(max_length=5)),
                ('summary', models.CharField(max_length=122)),
                ('report', models.ImageField(upload_to='satic/img', verbose_name='report')),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=5)),
                ('slot', models.CharField(max_length=10)),
                ('patient_name', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]