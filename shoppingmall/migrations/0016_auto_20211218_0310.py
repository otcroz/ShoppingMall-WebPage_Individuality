# Generated by Django 3.2.9 on 2021-12-18 03:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoppingmall', '0015_comment_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='delivery_fee',
            field=models.IntegerField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.IntegerField(max_length=15),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingmall.goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
