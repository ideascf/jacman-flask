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
    'posts': [site.article1, site.article1, site.article2, site.article2, site.article3, site.article3, ],
    'prev_link': '',
    'next_link': '',
    'path': '/',
    'list_number': False,
}


archive_page = {
    'archive': True,
    'year': 2016,
    'month': 3,
    'posts': [site.article1, site.article3]
}

archives_page = {
    'archive': True,
    'posts': [site.article1, site.article2, site.article3],
}

category_page = {
    'category': True,
    'posts': [site.article1, site.article1, site.article2, site.article2, site.article3, site.article3, ],
}

tag_page ={
    'tag': True,
    'posts': [site.article1, ],
}

tags_page = {
    'tag': True,
    'posts': [site.article1, site.article1, site.article2, site.article2, site.article3, site.article3, ],
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
    return render_template('categories.html')



@app.route('/categories/<category_id>')
def category(category_id):
    return render_template('category.html', page=category_page)


# @app.route('/archive/<year>/<month>')
# def archive(year, month):
@app.route('/archive/<year>/<month>/')
def archive(year, month):
    return render_template('archive.html', page=archive_page)

@app.route('/archives')
def archives():
    return render_template('archives.html', page=archives_page)


@app.route('/post/<article_id>')
def get_post(article_id):
    return render_template('post.html', page=site.article1, body='bodybody')


@app.route('/tag/<tag_id>')
def tag(tag_id):
    pass

@app.route('/tags')
def tags():
    return render_template('tag.html', page=tags_page)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
    # app.run(host='0.0.0.0', port=8888)
