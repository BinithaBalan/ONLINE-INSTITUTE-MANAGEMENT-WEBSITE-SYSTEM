# Generated by Django 3.2 on 2021-04-19 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_data_set_label_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('post_id', models.IntegerField()),
                ('msg', models.CharField(max_length=1500)),
                ('dt', models.CharField(max_length=30)),
                ('tm', models.CharField(max_length=15)),
            ],
        ),
    ]
