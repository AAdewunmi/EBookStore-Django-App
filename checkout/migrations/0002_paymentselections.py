# Generated by Django 5.0.7 on 2024-08-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentSelections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required', max_length=255, verbose_name='name')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Payment Selection',
                'verbose_name_plural': 'Payment Selections',
            },
        ),
    ]
