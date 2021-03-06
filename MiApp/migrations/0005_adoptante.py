# Generated by Django 4.0.4 on 2022-05-11 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0004_delete_adoptante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adoptante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreAdoptante', models.CharField(max_length=50)),
                ('apellidoAdoptante', models.CharField(max_length=50)),
                ('emailAdoptante', models.EmailField(max_length=254)),
                ('preferenciaAnimal', models.CharField(max_length=10)),
            ],
        ),
    ]
