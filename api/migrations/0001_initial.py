# Generated by Django 3.1.4 on 2020-12-23 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ShoeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(choices=[('R', 'Red'), ('O', 'Orange'), ('Y', 'Yellow'), ('G', 'Green'), ('B', 'Blue'), ('I', 'Indigo'), ('V', 'Violet'), ('BL', 'Black'), ('W', 'White')], default='W', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(default=1)),
                ('brand_name', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=100)),
                ('fasten_type', models.CharField(choices=[('V', 'Velcro'), ('SL', 'Shoe_Laces')], default='SL', max_length=2)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.shoecolor')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.manufacturer')),
                ('shoe_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.shoetype')),
            ],
        ),
    ]
