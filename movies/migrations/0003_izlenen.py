# Generated by Django 4.1.5 on 2023-06-17 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_katagori_tur_movies_katagori_movies_tur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Izlenen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izlenen', models.ManyToManyField(null=True, to='movies.movies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
