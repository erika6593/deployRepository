# Generated by Django 4.1 on 2024-04-08 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'product_types',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychology_tests.producttypes')),
            ],
            options={
                'db_table': 'quiz',
            },
        ),
        migrations.CreateModel(
            name='ProductPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='product_pictures/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychology_tests.quiz')),
            ],
            options={
                'db_table': 'product_pictures',
            },
        ),
    ]