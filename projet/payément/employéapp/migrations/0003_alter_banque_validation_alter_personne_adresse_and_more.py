# Generated by Django 4.1.4 on 2023-03-16 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employéapp', '0002_alter_recu_date_alter_recu_employe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banque',
            name='validation',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='personne',
            name='adresse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employéapp.adresse'),
        ),
        migrations.AlterField(
            model_name='personne',
            name='photo',
            field=models.ImageField(default='/static/photo/default.jpg', upload_to='static/photo'),
        ),
        migrations.AlterField(
            model_name='recu',
            name='employe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employéapp.employe'),
        ),
    ]
