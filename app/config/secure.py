# _*_ coding: utf-8 _*_
DEBUG = True

# Token 配置
SECRET_KEY = 'But you, Lord , are a shield around me, my glory, the One who lifts my head high.'  # 加密
TOKEN_EXPIRATION = 30 * 24 * 3600  # 有效期: 30天

# MySQL 数据库配置
SQLALCHEMY_DATABASE_URI = 'postgres://atzsrcjrnfaauu:f5b344ab9841661b4c5e8381a9474eb45fdb3d017e6faacf7ef853244b57a417@ec2-107-22-234-204.compute-1.amazonaws.com:5432/deaqbkvj1rtk6f'
SQLALCHEMY_ENCODING = 'utf-8'
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 屏蔽 sql alchemy 的 FSADeprecationWarning
