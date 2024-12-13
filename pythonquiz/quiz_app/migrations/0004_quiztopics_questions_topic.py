# Generated by Django 4.1.13 on 2024-12-12 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0003_userresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizTopics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='topic',
            field=models.CharField(default='', max_length=200),
        ),
    ]
