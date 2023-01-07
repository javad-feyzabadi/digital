# Generated by Django 3.2 on 2023-01-07 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20230107_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'audio'), (2, 'video'), (3, 'pdf')], default=1, verbose_name='file type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='products.product', verbose_name='product'),
        ),
    ]
