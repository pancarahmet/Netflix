# Generated by Django 4.1.5 on 2023-06-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filmismi', models.CharField(max_length=100, verbose_name='Film Adı')),
                ('aciklama', models.TextField(max_length=400, verbose_name='Film Açıklması')),
                ('afis', models.FileField(blank=True, null=True, upload_to='afisler', verbose_name='Film Afişi')),
            ],
        ),
    ]
