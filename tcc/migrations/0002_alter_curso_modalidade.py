# Generated by Django 4.0.6 on 2022-08-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='modalidade',
            field=models.CharField(choices=[('Bacharelado', 'Bacharelado'), ('Licenciatura', 'Licenciatura'), ('Tecnólogo', 'Tecnólogo')], max_length=30),
        ),
    ]
