from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """
        Django生成的表名前缀为应用名之后跟上模型（model）的小写（blog_post）
    """
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    """
        slug是一个短标签，该标签只包含字母，数字，下划线或连接线;
        通过使用slug字段给我们的blog帖子构建漂亮的，友好的URLs;
        给该字段添加了unique_for_date参数，这样我们就可以使用日期和帖子的slug来为所有帖子构建URLs;
        在相同的日期中Django会阻止多篇帖子拥有相同的slug。
    """
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    """    
        ForeignKey这个字段定义了一个多对一（many-to-one）的关系;
        告诉Django一篇帖子只能由一名用户编写，一名用户能编写多篇帖子;
        我们关联上了Django权限系统的User模型（model）;
        我们通过related_name属性指定了从User到Post的反向关系名.
    """
    author = models.ForeignKey(User,
                               related_name='blog_posts',
                               on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    """
        choices参数，这样这个字段的值只能是给予的选择参数中的某一个值
    """
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        """
        告诉Django查询数据库的时候默认返回的是根据publish字段进行降序排列过的结果。
        我们使用负号来指定进行降序排列
        """
        ordering = ('-publish',)

    def __str__(self):
        """
            Python3中所有的strings都使用unicode，因此我们只使用str()方法。unicode()方法已经废弃
        """
        return self.title

