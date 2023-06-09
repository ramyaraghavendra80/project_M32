# Generated by Django 4.2 on 2023-05-27 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoplane', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCartView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_id', models.IntegerField()),
                ('product_id', models.IntegerField(default='')),
                ('user_id', models.IntegerField()),
                ('comment', models.CharField(max_length=1000)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('email_id', models.CharField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(default=1),
        ),
    ]
