# Generated by Django 3.2.19 on 2023-06-14 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20230613_1705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AlterField(
            model_name='patient',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
