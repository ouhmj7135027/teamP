# Generated by Django 2.2.3 on 2019-07-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_name', models.CharField(max_length=50, verbose_name='카테고리')),
                ('image', models.FileField(upload_to='images/')),
                ('description', models.CharField(max_length=500, verbose_name='처리방법')),
                ('tag', models.CharField(choices=[('페트', '페트병'), ('일반', '일반쓰레기'), ('음식물', '음식물쓰레기'), ('유리', '유리'), ('병', '병'), ('대형', '대형폐기물'), ('종이', '종이'), ('종이팩', '종이팩'), ('금속캔', '금속캔'), ('유리병', '유리병')], max_length=20)),
            ],
        ),
    ]
