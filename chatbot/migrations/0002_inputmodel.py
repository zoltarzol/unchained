# Generated by Django 4.1.3 on 2022-12-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_msg', models.TextField(default='', max_length=1000, null=True)),
            ],
        ),
    ]
