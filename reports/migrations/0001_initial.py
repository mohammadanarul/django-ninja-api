# Generated by Django 4.1.6 on 2023-02-08 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostReport",
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
                ("text", models.CharField(max_length=300)),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (1, "Spam"),
                            (2, "Nudity"),
                            (3, "Unauthorized Sales"),
                            (4, "Violence"),
                            (5, "Terrorism"),
                            (6, "Hate Speech"),
                            (7, "False Information"),
                            (8, "Suicide Of Self Injury"),
                            (9, "Harassment"),
                            (10, "Something Else"),
                        ]
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.post"
                    ),
                ),
            ],
        ),
    ]