# Generated by Django 5.0.4 on 2024-04-17 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_customer_id_customer_customerix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customerIx',
        ),
        migrations.AddField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, default=3, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
