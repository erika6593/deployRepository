# Generated by Django 4.1 on 2024-04-09 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychology_tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productpictures',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='productpictures',
            name='order',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
