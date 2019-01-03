from mongoengine import *

connect('DB', username='xmzd', password='1234')


class Users(Document):
    account = StringField(required=True)
    password = StringField(required=True)

    @classmethod
    def create(cls, account, pwd):
        return cls(account=account, password=pwd).save()

    @classmethod
    def get_by_id(cls, uid):
        return cls.objects.with_id(uid)

    @classmethod
    def get_by_email(cls, email):
        try:
            return cls.objects.get(account=email)
        except DoesNotExist:
            return None


















# from django.db import models
# from datetime import datetime
#
# # Create your models here.
#
#
# class BookInfo(models.Model):
#     # 图书名称
#     btitle = models.CharField(max_length=20)
#     # 阅读量
#     bread = models.IntegerField(default=0)
#     # 评论量
#     bcomment = models.IntegerField(default=0)
#     # 删除标记
#     isDelete = models.BooleanField(default=False)
#
#     # 让模型类生成的 表名 不依赖 应用名(project/apps/users)
#     class Meta:
#         db_table = 'book'
#
#
# class HeroInfo(models.Model):
#     # 英雄名
#     hname = models.CharField(max_length=20)
#     # 性别
#     hgender = models.BooleanField(default=False)
#     # 备注
#     hcomment = models.CharField(max_length=200)
#     # 关系属性
#     hbook = models.ForeignKey('BookInfo', id)
#     # 删除标记
#     isDelete = models.BooleanField(default=False)
#
#     class Meta:
#         db_table = 'hero'