# Generated by Django 4.2.4 on 2023-11-26 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_profesion_options_contacto_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='apellido',
            field=models.CharField(help_text='Ingresa tu apellido', max_length=100),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(help_text='Ingresa tu nombre', max_length=100),
        ),
    ]
