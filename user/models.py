#!/usr/bin/python
#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField('名字', max_length=20, blank=True)
    user_number = models.CharField('学号', max_length=20, blank=True)

    class Meta(AbstractUser.Meta):
        pass


