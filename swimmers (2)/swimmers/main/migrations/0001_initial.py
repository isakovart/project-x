# Generated by Django 3.2.9 on 2022-06-14 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, verbose_name='Name')),
                ('Date', models.DateField(max_length=255, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Award',
                'verbose_name_plural': 'Awards',
            },
        ),
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.IntegerField(max_length=255, verbose_name='Name')),
                ('Content', models.TextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Fact',
                'verbose_name_plural': 'Facts',
            },
        ),
        migrations.CreateModel(
            name='Swimmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, verbose_name='Name')),
                ('Age', models.IntegerField(verbose_name='Age')),
                ('Weight', models.IntegerField(max_length=255, verbose_name='Weight')),
                ('Awards', models.ManyToManyField(to='main.Award', verbose_name='Awards')),
                ('Facts', models.ManyToManyField(to='main.Fact', verbose_name='Facts')),
            ],
            options={
                'verbose_name': 'Swimmer',
                'verbose_name_plural': 'Swimmers',
            },
        ),
    ]
