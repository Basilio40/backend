# Generated by Django 4.1.1 on 2022-09-29 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listacompras',
            name='concluido',
            field=models.BooleanField(default=False),
        ),
    ]
