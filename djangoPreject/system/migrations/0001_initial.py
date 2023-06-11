# Generated by Django 4.2 on 2023-04-10 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, null=True, verbose_name='类别')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='标题')),
                ('author', models.CharField(max_length=255, null=True, verbose_name='作者')),
                ('createTime', models.CharField(max_length=255, null=True, verbose_name='发布时间')),
                ('press', models.CharField(max_length=255, null=True, verbose_name='出版社')),
                ('now_price', models.FloatField(default=0, verbose_name='现价')),
                ('pre_price', models.FloatField(default=0, verbose_name='原价')),
                ('discount', models.FloatField(default=0, verbose_name='折扣')),
                ('detail', models.TextField(null=True, verbose_name='详情')),
                ('star', models.IntegerField(default=0, verbose_name='评分')),
                ('comment_num', models.IntegerField(default=0, verbose_name='评论数量')),
                ('img_url', models.CharField(max_length=255, null=True, verbose_name='图片链接')),
                ('book_url', models.CharField(max_length=255, null=True, verbose_name='书籍链接')),
                ('addTime', models.CharField(max_length=255, null=True, verbose_name='采集时间')),
            ],
            options={
                'verbose_name': '书籍信息',
                'verbose_name_plural': '书籍信息',
                'db_table': 'booktable',
            },
        ),
    ]
