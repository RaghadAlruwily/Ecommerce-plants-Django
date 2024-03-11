# Generated by Django 4.2.10 on 2024-03-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_itemdetails_desc_itemdetails_fertilization_and_more'),
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
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]