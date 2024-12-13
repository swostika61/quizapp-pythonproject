# Generated by Django 4.1.13 on 2024-12-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Questions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=200)),
                ("option1", models.CharField(max_length=200)),
                ("option2", models.CharField(max_length=200)),
                ("option3", models.CharField(max_length=200)),
                ("option4", models.CharField(max_length=200)),
                ("answer", models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(name="Question",),
    ]
