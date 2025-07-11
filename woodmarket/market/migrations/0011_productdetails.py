# Generated by Django 5.2 on 2025-06-01 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0010_tag_product_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(blank=True, max_length=100)),
                ('size', models.CharField(blank=True, max_length=100)),
                ('warranty_years', models.PositiveIntegerField(default=0)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='market.product')),
            ],
        ),
    ]
