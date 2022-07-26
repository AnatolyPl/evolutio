# Generated by Django 3.2.7 on 2022-07-19 16:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipped', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_total', models.FloatField()),
                ('date_of_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('brand_id', models.IntegerField()),
                ('reference', models.CharField(max_length=150)),
                ('customer_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_api.customer')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('delivery_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_api.delivery')),
                ('product_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_api.product')),
            ],
        ),
        migrations.AddField(
            model_name='delivery',
            name='delivery_product',
            field=models.ManyToManyField(through='test_api.DeliveryProduct', to='test_api.Product'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='order_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_api.order'),
        ),
    ]
