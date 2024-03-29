# Generated by Django 3.2.9 on 2021-12-13 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingmall', '0012_auto_20211213_0350'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='case_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoppingmall.casetype'),
        ),
    ]
