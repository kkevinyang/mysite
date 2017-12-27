from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    """
    list_display属性允许你在设置一些你想要在管理对象列表页面显示的模型（model）字段;
    通过使用search_fields属性定义了一个搜索字段列;
    有个可以通过时间层快速导航的栏，该栏通过定义date_hierarchy属性出现；
    通过使用ordering属性使得帖子通过Status和Publish列进行排序；
    通过使用prepopulated_fields属性告诉Django通过输入的标题来填充slug字段；
    author字段展示显示为了一个搜索控件
    """
    list_display = ('title', 'slug', 'author', 'publish', 'status')  # 显示字段
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')  # 搜索栏
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Post, PostAdmin)

