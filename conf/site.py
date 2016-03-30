# coding=utf-8
import datetime

tag1 = {'id': 1, 'path': 'tag/java', 'name': 'java', 'posts': ['post1', 'post2']}
tag2 = {'id': 2, 'path': 'tag/go', 'name': 'go', 'posts': ['post1', 'post3']}
tag3 = {'id': 3, 'path': 'tag/python', 'name': 'python', 'posts': ['post1', 'post2', 'post4']}

category1 = {'id': 1, 'posts': ['post1', 'post2'], 'path': 'categories/category1', 'name': 'category1', 'parent': None}
category2 = {'id': 2, 'posts': ['post3', ], 'path': 'categories/category2', 'name': 'category2', 'parent': None}


article1 = {
    'id': 1,
    'title': 'title-right',  # 标题
    'date': datetime.datetime.now(),  # 创建日期
    'updated': datetime.datetime.now(),  # 修改日期
    'toc': True,  # 是否显示目录
    'comments': '',  # 注释
    'layout': 'post',  # 本文使用的布局
    'content': 'content-testtest',  # 文章内容
    'categories': [category1, category2],  # 文章所加标签
    'tags': [tag1, tag2],
    'excerpt': 'excerpt-test',  # 文章摘要
    'more': 'more-test',  #
    'source': 'source-test',
    'full_source': 'full_source-test',
    'path': 'post',  # 文章对应的path(非完整链接),如 /post/article1
    'permalink': 'permalink-test',  # 永久链接
    'prev': None,  # 上一篇
    'next': None,  # 下一篇
    'raw': 'raw-test',  #
    'photos': [],  # 文章使用的图片
    'link': '/post/1',  # 文章对应的链接(完整链接地址)
}


article3 = {
    'id': 3,
    'title': 'title-left',  # 标题
    'date': datetime.datetime.now(),  # 创建日期
    'updated': datetime.datetime.now(),  # 修改日期
    'toc': True,  # 是否显示目录
    'comments': '',  # 注释
    'layout': 'post',  # 本文使用的布局
    'content': 'content-testtest',  # 文章内容
    'categories': [category1, category2],  # 文章所加标签
    'tags': [tag1, tag3],
    'excerpt': 'excerpt-test',  # 文章摘要
    'more': 'more-test',  #
    'source': 'source-test',
    'full_source': 'full_source-test',
    'path': 'post',  # 文章对应的path(非完整链接),如 /post/article1
    'permalink': 'permalink-test',  # 永久链接
    'prev': None,  # 上一篇
    'next': None,  # 下一篇
    'raw': 'raw-test',  #
    'photos': [],  # 文章使用的图片
    'link': 'post/3',  # 文章对应的链接(完整链接地址)
}

article2 = {
    'id': 2,
    'title': 'title-test',  # 标题
    'date': datetime.datetime.strptime('2016-02-03 11:00:00', '%Y-%m-%d %H:%M:%S'),  # 创建日期
    'updated': datetime.datetime.now(),  # 修改日期
    'toc': True,  # 是否显示目录
    'comments': '',  # 注释
    'layout': 'post',  # 本文使用的布局
    'content': 'content-testtest',  # 文章内容
    'categories': [category1, category2],  # 文章所加标签
    'tags': [tag2, tag3],
    'excerpt': 'excerpt-test',  # 文章摘要
    'more': 'more-test',  #
    'source': 'source-test',
    'full_source': 'full_source-test',
    'path': 'post',  # 文章对应的path(非完整链接),如 /post/article1
    'permalink': 'permalink-test',  # 永久链接
    'prev': article1,  # 上一篇
    'next': article3,  # 下一篇
    'raw': 'raw-test',  #
    'photos': [],  # 文章使用的图片
    'link': 'post/2',  # 文章对应的链接(完整链接地址)
}


tags = [tag1, tag2, tag3]
categories = [category1, category2]
posts = [article1, article2, article3]

archive_dir = '/archive'

timezone = 'UTC+8'  # 时区

lang = 'zh'  # 语言

path = {
    'category': 'category',
}