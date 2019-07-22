from django.db import models

# Create your models here.


class User(models.Model):
    SEX_CHOICES = (
        ('male', "男"),
        ('female', "女"),
    )
    STATUS_CHOICES = (
        (0, '启用'),
        (1, '禁用'),
    )
    username = models.CharField(max_length=64, unique=True, verbose_name='用户名')
    nickname = models.CharField(max_length=64, blank=True, null=True, verbose_name='昵称')
    password = models.CharField(max_length=256, verbose_name='密码')
    email = models.EmailField(unique=True, verbose_name='邮箱')
    sex = models.CharField(max_length=32, choices=SEX_CHOICES, default="男", verbose_name='性别')
    status = models.SmallIntegerField(default=0, choices=STATUS_CHOICES, verbose_name='账号状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.username + ', ' + self.nickname

    class Meta:
        ordering = ["-create_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class LoginLog(models.Model):
    event_type_choice = (
        (0, '其他'),
        (1, '登陆'),
        (2, '退出'),
        (3, '登陆错误'),
        (4, '修改密码失败'),
        (5, '修改密码成功'),
    )
    user = models.ForeignKey('User', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='用户名')
    event_type = models.SmallIntegerField('事件类型', choices=event_type_choice, default=1)
    detail = models.TextField('事件详情', default='登陆成功')
    address = models.GenericIPAddressField('IP地址', blank=True, null=True)
    useragent = models.CharField(max_length=512, blank=True, null=True, verbose_name='User_Agent')
    create_time = models.DateTimeField('事件时间', auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ["-create_time"]
        verbose_name = '登陆日志'
        verbose_name_plural = '登陆日志'

