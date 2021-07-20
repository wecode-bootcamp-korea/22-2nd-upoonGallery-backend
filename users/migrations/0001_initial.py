# Generated by Django 3.2.5 on 2021-07-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reviews', '0001_initial'),
        ('arts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('kakao_id', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('nick_name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=30, null=True)),
                ('reviewed_arts', models.ManyToManyField(related_name='reviewed_users', through='reviews.Review', to='arts.Art')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
