# Generated by Django 3.2.7 on 2021-11-22 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('conteudo', models.TextField()),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
    ]