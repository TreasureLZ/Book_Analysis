from django.db import models

class Book(models.Model):
    category = models.CharField(verbose_name="类别",max_length=255,null=True)
    title = models.CharField(verbose_name="标题",max_length=255,null=True)
    author = models.CharField(verbose_name="作者",max_length=255,null=True)
    createTime = models.CharField(verbose_name="发布时间",max_length=255,null=True)
    press = models.CharField(verbose_name="出版社",max_length=255,null=True)
    now_price = models.FloatField(verbose_name="现价", default=0)
    pre_price = models.FloatField(verbose_name="原价", default=0)
    discount = models.FloatField(verbose_name="折扣", default=0)
    detail = models.TextField(verbose_name='详情',null=True)
    star = models.IntegerField(verbose_name="评分", default=0)
    comment_num = models.IntegerField(verbose_name="评论数量", default=0)
    img_url = models.CharField(verbose_name='图片链接',max_length=255,null=True)
    book_url = models.CharField(verbose_name='书籍链接',max_length=255,null=True)
    addTime = models.CharField(verbose_name='采集时间',max_length=255,null=True)

    class Meta:
        verbose_name = "书籍信息"
        verbose_name_plural = "书籍信息"
        db_table = "booktable"
        
    def short_detail(self):
        if len(str(self.detail)) > 10:
            return '{}...'.format(str(self.detail)[0:9])
        else:
            return str(self.detail)

    short_detail.allow_tags = True
    short_detail.short_description = '详情'
    
    
    
    def short_title(self):
        if len(str(self.title)) > 10:
            return '{}...'.format(str(self.title)[0:9])
        else:
            return str(self.title)
        
    short_title.allow_tags = True
    short_title.short_description = '标题'