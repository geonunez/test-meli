# Generated by Django 2.0.6 on 2018-06-15 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dna', models.TextField(unique=True)),
                ('is_mutant', models.BooleanField(default=False)),
            ],
        ),
    ]
