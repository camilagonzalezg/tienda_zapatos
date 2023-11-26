# Generated by Django 4.2.4 on 2023-11-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_producto_imagen1_producto_imagen2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Ingresa tu email', max_length=100)),
                ('asunto', models.CharField(help_text='Ingresa tu ausnto', max_length=100)),
                ('mensaje', models.CharField(help_text='Ingresa tu mensaje', max_length=100)),
                ('copia', models.BooleanField(default=False, help_text='¿Con copia?')),
            ],
        ),
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profesion', models.CharField(help_text='Ingresa tu profesion', max_length=200)),
            ],
        ),
    ]
