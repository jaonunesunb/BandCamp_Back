# Generated by Django 4.1.7 on 2023-02-25 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Mensagem de erro customizada'}, max_length=127, unique=True),
        ),
    ]