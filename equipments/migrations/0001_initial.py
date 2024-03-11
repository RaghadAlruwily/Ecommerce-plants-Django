# Generated by Django 4.2.10 on 2024-03-10 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_product', models.IntegerField()),
                ('id_user', models.IntegerField()),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('tax', models.FloatField()),
                ('image', models.CharField(max_length=150, null=True)),
                ('total', models.FloatField()),
                ('discount', models.FloatField()),
                ('net', models.FloatField(null=True)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ItemDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('plantsize', models.IntegerField(null=True)),
                ('desc', models.CharField(max_length=1000, null=True)),
                ('temp', models.FloatField(null=True)),
                ('light', models.CharField(max_length=150, null=True)),
                ('water', models.CharField(max_length=150, null=True)),
                ('fertilization', models.CharField(max_length=150, null=True)),
                ('qty', models.IntegerField()),
                ('tax', models.FloatField()),
                ('image', models.CharField(max_length=150, null=True)),
                ('total', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('itemsid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='equipments.items')),
            ],
        ),
    ]
