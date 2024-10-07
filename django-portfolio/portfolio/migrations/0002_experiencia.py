# Generated by Django 5.1.1 on 2024-10-07 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion_del_curso', models.CharField(max_length=255)),
                ('descripcion_curso', models.TextField()),
                ('fecha_curso', models.DateField()),
                ('numero_horas', models.IntegerField()),
            ],
        ),
    ]
