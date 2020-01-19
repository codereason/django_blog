from django.apps import AppConfig

'''
这些是我们在运行 startapp 创建 blog 应用时自动生成的代码，可以看到有一个 BlogConfig 类
，其继承自 AppConfig 类，看名字就知道这是和应用配置有关的类。我们可以通过设置这个类中的一些属性的值来配置这个应用的一些特性的。
比如这里的 name 是用来定义 app 的名字，需要和应用名保持一致，不要改。要修改 app 在 admin 后台的显示名字，添加 verbose_name 属性。

'''
class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = '博客'