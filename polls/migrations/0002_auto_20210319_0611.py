# Generated by Django 3.0.5 on 2021-03-19 06:11

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=djongo.models.fields.ArrayReferenceField(on_delete=djongo.models.fields.ArrayReferenceField._on_delete, to='polls.polls'),
        ),
    ]