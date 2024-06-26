# Generated by Django 4.2.4 on 2023-08-14 14:21

# Python imports
import uuid

# Django imports
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BookedShowDetail",
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
                ("show_date", models.DateField()),
                ("available_seats", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("release_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Screen",
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
                ("screen_number", models.IntegerField()),
                ("total_seat", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ScreenSeatTypesMapping",
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
                (
                    "seat_type",
                    models.CharField(
                        choices=[
                            ("PLATINUM", "Platinum"),
                            ("GOLD", "Gold"),
                            ("SILVER", "Silver"),
                            ("UNKNOW", "Unknown"),
                        ],
                        default="UNKNOW",
                        max_length=10,
                    ),
                ),
                (
                    "screen",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seat_screen",
                        to="movie.screen",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShowDetail",
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
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                ("available_seats", models.IntegerField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="showtime_movie",
                        to="movie.movie",
                    ),
                ),
                (
                    "screen",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="showtime_screen",
                        to="movie.screen",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ShowSeatPrice",
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
                ("price", models.FloatField()),
                (
                    "seat_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seat_price",
                        to="movie.screenseattypesmapping",
                    ),
                ),
                (
                    "show_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="show_price_detail",
                        to="movie.showdetail",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Seat",
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
                ("seat_number", models.CharField(max_length=10)),
                ("raw", models.CharField(max_length=1)),
                ("col", models.CharField(max_length=1)),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="seat_type_screen",
                        to="movie.screenseattypesmapping",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
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
                (
                    "booked_show",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="booking_booked_show",
                        to="movie.bookedshowdetail",
                    ),
                ),
                (
                    "seats",
                    models.ManyToManyField(
                        related_name="booking_seats", to="movie.seat"
                    ),
                ),
                (
                    "showtime",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="booking_showtime",
                        to="movie.showdetail",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="booking_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bookedshowdetail",
            name="show_detail",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="booked_show_detail",
                to="movie.showdetail",
            ),
        ),
    ]
