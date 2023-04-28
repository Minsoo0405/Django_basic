# Generated by Django 4.2 on 2023-04-28 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_answer_voter_question_voter_alter_answer_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('nation', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('league', models.CharField(max_length=50)),
            ],
        ),
    ]
