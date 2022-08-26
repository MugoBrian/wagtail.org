# Generated by Django 3.2.12 on 2022-08-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("short_title", models.CharField(blank=True, max_length=64)),
                (
                    "icon",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("arrow", "Arrow"),
                            ("arrow-alt", "Arrow alt"),
                            ("arrow-in-circle", "Arrow in circle"),
                            ("arrow-in-square", "Arrow in square"),
                            ("arrows", "Arrows"),
                            ("blog", "Blog"),
                            ("bread", "Bread"),
                            ("briefcase", "Briefcase"),
                            ("building", "Building"),
                            ("calendar", "Calendar"),
                            ("document", "Document"),
                            ("envelope", "Envelope"),
                            ("explanation", "Explanation"),
                            ("eye", "Eye"),
                            ("flame", "Flame"),
                            ("friends", "Friends"),
                            ("github", "Github"),
                            ("handshake", "Handshake"),
                            ("heart", "Heart"),
                            ("history", "History"),
                            ("id-card", "ID Card"),
                            ("image", "Image"),
                            ("knife-fork", "Knife Fork"),
                            ("leaf", "Leaf"),
                            ("location-pin", "Location Pin"),
                            ("map", "Map"),
                            ("money", "Money"),
                            ("moon", "Moon"),
                            ("one-two-steps", "One Two Steps"),
                            ("padlock-dark", "Padlock Dark"),
                            ("padlock-light", "Padlock Light"),
                            ("paper-plane", "Paper Plane"),
                            ("paper-stack", "Paper Stack"),
                            ("pen-checkbox", "Pen Checkbox"),
                            ("person-in-tie", "Person in Tie"),
                            ("python", "Python"),
                            ("question-mark-circle", "Question Mark Circle"),
                            ("quotes", "Quotes"),
                            ("release-cycle", "Release Cycle"),
                            ("roadmap", "Roadmap"),
                            ("rocket", "Rocket"),
                            ("rollback", "Rollback"),
                            ("slack", "Slack"),
                            ("speech-bubble", "Speech Bubble"),
                            ("sun-cloud-dark", "Sun Cloud Dark"),
                            ("sun-cloud-light", "Sun Cloud Light"),
                            ("table-tennis", "Table Tennis"),
                            ("tree", "Tree"),
                            ("wordpress", "Wordpress"),
                            ("world", "World"),
                        ],
                        max_length=255,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
    ]