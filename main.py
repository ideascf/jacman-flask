# coding=utf-8
import copy
import datetime
from flask import Flask
from flask import render_template, url_for

from util.tools import *
from conf import theme, site
from conf.site import tag1, tag2, tag3, category1, category2
app = Flask(__name__)


# filter
def sorted_tags_by_posts(tags):
    """

    :param tags:
    :type tags: list
    :return:
    :rtype: list
    """

    tags = copy.copy(tags)
    tags.sort(key=lambda tag: len(tag['posts']), reverse=True)

    return tags

app.add_template_filter(sorted_tags_by_posts)

tinysou_search = {
    'enable': True,
    'id': 1,
}


item = {
    'content': 'item-content',
}

article_left = {
    'title': 'title-right',  # 标题
    'date': datetime.datetime.now(),  # 创建日期
    'updated': datetime.datetime.now(),  # 修改日期
    'toc': True,  # 是否显示目录
    'comments': '',  # 注释
    'layout': 'post',  # 本文使用的布局
    'content': 'content-testtest',  # 文章内容
    'categories': [category1, category2],  # 文章所加标签
    'excerpt': 'excerpt-test',  # 文章摘要
    'more': 'more-test',  #
    'source': 'source-test',
    'full_source': 'full_source-test',
    'path': 'path_test',  # 文章对应的path(非完整链接),如 /post/article1
    'permalink': 'permalink-test',  # 永久链接
    'prev': None,  # 上一篇
    'next': None,  # 下一篇
    'raw': 'raw-test',  #
    'photos': [],  # 文章使用的图片
    'link': 'post/link-test',  # 文章对应的链接(完整链接地址)
}


article_right = {
    'title': 'title-left',  # 标题
    'date': datetime.datetime.now(),  # 创建日期
    'updated': datetime.datetime.now(),  # 修改日期
    'toc': True,  # 是否显示目录
    'comments': '',  # 注释
    'layout': 'post',  # 本文使用的布局
    'content': 'content-testtest',  # 文章内容
    'categories': [category1, category2],  # 文章所加标签
    'excerpt': 'excerpt-test',  # 文章摘要
    'more': 'more-test',  #
    'source': 'source-test',
    'full_source': 'full_source-test',
    'path': 'path_test',  # 文章对应的path(非完整链接),如 /post/article1
    'permalink': 'permalink-test',  # 永久链接
    'prev': None,  # 上一篇
    'next': None,  # 下一篇
    'raw': 'raw-test',  #
    'photos': [],  # 文章使用的图片
    'link': 'post/link-test',  # 文章对应的链接(完整链接地址)
}

article = {
    'title': 'title-test',  # 标题
    'date': datetime.datetime.now(),  # 创建日期
    'updated': datetime.datetime.now(),  # 修改日期
    'toc': True,  # 是否显示目录
    'comments': '',  # 注释
    'layout': 'post',  # 本文使用的布局
    'content': 'content-testtest',  # 文章内容
    'categories': [category1, category2],  # 文章所加标签
    'excerpt': 'excerpt-test',  # 文章摘要
    'more': 'more-test',  #
    'source': 'source-test',
    'full_source': 'full_source-test',
    'path': 'path_test',  # 文章对应的path(非完整链接),如 /post/article1
    'permalink': 'permalink-test',  # 永久链接
    'prev': article_left,  # 上一篇
    'next': article_right,  # 下一篇
    'raw': 'raw-test',  #
    'photos': [],  # 文章使用的图片
    'link': 'post/link-test',  # 文章对应的链接(完整链接地址)
}


article_page = {
    'title': 'title-test',  # 标题
    'date': datetime.datetime.now(),  # 创建日期
    'updated': datetime.datetime.now(),  # 修改日期
    'toc': True,  # 是否显示目录
    'comments': '',  # 注释
    'layout': 'post',  # 本文使用的布局
    'content': 'content-testtest',  # 文章内容
    'excerpt': 'excerpt-test',  # 文章摘要
    'more': 'more-test',  #
    'source': 'source-test',
    'full_source': 'full_source-test',
    'path': 'path_test',  # 文章对应的URL
    'permalink': 'permalink-test',  # 永久链接
    'prev': 'prev-test',  # 上一篇
    'next': 'next-test',  # 下一篇
    'raw': 'raw-test',  #
    'photos': [],  # 文章使用的图片
    'link': '/post/link-test',  # 链接
}

post_page = {
    'published': True,
    'categories': [category1, category2],
    'tags': [tag1, tag2]
}

home_page = {
    'title': 'title-test',
    'per_page': 20,
    'total': 100,
    'current': 1,
    'current_url': '/',
    'posts': [article_page, article_page, article_page, article_page, article_page, article_page, ],
    'prev_link': '',
    'next_link': '',
    'path': '/',
    'list_number': False,
}

archive_page = {
    'archive': True,
    'year': 2016,
    'month': 12,
    'posts': [article_page, ]
}

category_page = {
    'category': 'category1',
}

tag_page = {
    'tag': 'tag1',
}

@app.context_processor
def util_for_blog():
    return dict(

    )

app.jinja_env.globals.update(
    gettext=gettext,
    toc=toc,
    list_archives=list_archives,
    list_categories=list_categories,
    tagcloud=tagcloud,
    date_xml=date_xml,
    root_for=root_for,
    cur_year=cur_year,
    open_graph=open_graph,
    is_post=is_post,

    config=theme,
    theme=theme,
    site=site,
    tinysou_search=tinysou_search,

    item=item,
    page=home_page,
)


@app.route('/categories')
def categories():
    return 'category'


@app.route('/categories/<category_id>')
def category(category_id):
    return render_template('category.html', page=category_page)


@app.route('/archives')
def archive():
    return render_template('archive.html', page=archive_page)


@app.route('/post/<article_id>')
def get_post(article_id):
    return render_template('post.html', page=article, body='bodybody')


@app.route('/path-test')
def path_test():
    pass


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
    # app.run(host='0.0.0.0', port=8888)
