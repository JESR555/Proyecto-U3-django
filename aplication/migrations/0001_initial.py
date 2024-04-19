# Generated by Django 5.0.2 on 2024-04-18 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                ("nombre", models.CharField(max_length=100)),
                ("descripcion", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Videojuego",
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
                ("titulo", models.CharField(max_length=200)),
                ("descripcion", models.TextField()),
                ("desarrollador", models.CharField(max_length=100)),
                ("fecha_lanzamiento", models.DateField()),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "imagen",
                    models.ImageField(blank=True, null=True, upload_to="videojuegos/"),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="aplication.categoria",
                    ),
                ),
            ],
        ),
    ]