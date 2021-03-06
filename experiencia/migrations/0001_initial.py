# Generated by Django 3.2 on 2021-05-09 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50)),
                ('cargo', models.URLField()),
                ('contenido', models.CharField(max_length=200)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='experiencia')),
                ('inicio', models.CharField(max_length=50)),
                ('fin', models.CharField(max_length=50)),
                ('url', models.URLField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Experiencia',
                'verbose_name_plural': 'Experiencias',
            },
        ),
    ]
