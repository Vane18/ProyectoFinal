# Generated by Django 4.0.4 on 2022-05-11 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0002_delete_animal_remove_adoptante_apellidoadoptante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreAnimal', models.CharField(max_length=50)),
                ('edadAnimal', models.IntegerField()),
                ('tipoAnimal', models.CharField(max_length=50)),
            ],
        ),
    ]
