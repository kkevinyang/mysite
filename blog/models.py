from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                    self).get_queryset().filter(status='published')


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
    # 创建一个管理器
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.
    tags = TaggableManager()

    # Django的惯例是给模型（model）添加get_absolute_url()方法用来返回一个对象的标准URL
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])

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


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)  # active布尔字段用来手动禁用那些不合适的评论

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
