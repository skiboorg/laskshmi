# Generated by Django 2.1.5 on 2019-01-30 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20190115_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='client',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Корзина клиента'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='guest',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='customuser.Guest', verbose_name='Корзина гостя'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='item.Item', verbose_name='Товар'),
        ),
    ]
