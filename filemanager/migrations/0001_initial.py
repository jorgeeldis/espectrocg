# Generated by Django 4.2.11 on 2024-04-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='media/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]