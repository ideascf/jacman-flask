# coding=utf-8
menu = [
    {'title': 'home', 'path': '/'},
    {'title': 'categories', 'path': 'categories'},
    {'title': 'archives', 'path': 'archives'},
    {'title': 'tags', 'path': 'tags'},
    {'title': 'about', 'path': 'about'},
]

title = "joychen's blog"

menu = menu  # 标题栏菜单


# 文章目录控制
toc = {
    'article': True,
    'aside': True,
}

# author = {
#     'tsina': 'sina weibo',
#     'weibo_verifier': 'weibo_verifier....',
#     'github': 'ideascf',
#     'douban': 'wuchong1014',
#
# }

author = 'joychen'

links = {
    'manong': 'https://coderq.com,programmer share...',
    'joychen': 'http://wuchong.me',
}

root = 'http://localhost:8888/'

index = {
    'expand': True,
    'excerpt_link': 'Read More',
}

date_format = '%Y-%m-%d'

imglogo = {
    'enable': True,
    'src': 'static/img/logo.png'
}

show_article_desc = True

google_analytics = {
    'enable': False,
    'id': '',
    'site': ''
}

baidu_tongji = {
    'enable': False,
    'sitecode': '',
}

cnzz_tongji = {
    'enable': False,
    'siteid': ''
}



google_cse = {
    'enable': False,
    'cx': '',
}

baidu_search = {
    'enable': False,
    'id': '',
    'site': '',
}

tinysou_search = {
    'enable': False,
    'id': '',
}

# 'widgets': ['github-card', 'category', 'tag', 'link', 'douban', 'rss', 'weibo']
widgets = ['github-card', 'rss', ]


# 归档配置
archive_conf = {
    'format': '%Y-%m-%d',
    'archive_dir': '/archives',
    'type': 'monthly',
    'style': '',
    'show_count': True,
    'transform': None,
    'separator': ', ',
    'class_name': 'archive',
    'reverse': False,
}

# social share
jiathis = {
    'enable': False,
}