# coding=utf-8
import copy
import datetime
import re
from flask import Flask
from flask import render_template

app = Flask(__name__)

# function


def gettext(str):
    return str


def toc(str, config=None):
    return str


def list_archives():
    """
    返回归档文件
    :return:
    """

    return []


def tagcloud():
    """
    返回标签云
    :return:
    """

    return ''


def date_xml(date):
    pass


def root_for(path):
    """

    :param path:
    :type path: str
    :return:
    """

    path = path or '/'
    root = config['root']
    if path.startswith(root):
        if path[0] == '/':
            path = root[0:-1] + path
        else:
            path = root + path

    return path

def open_graph(data):
    pass

def css(file):
    # 将.style文件编译为css文件
    pass

def cur_year():
    """

    :return:
    :rtype: str
    """

    return str(datetime.datetime.now().year)

def strip_html(str):
    """

    :param str:
    :return:
    :rtype: str
    """
    pass

def get_article_desc(article_str):
    """

    :param article_str:
    :type article_str: str
    :return:
    :rtype: str
    """

    s = strip_html(article_str)
    s = s.strip()

    return s[:140]

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


config = {
    'root': '/home/'
}

site = {
    'tags': [
        {'path': '/path/java', 'name': 'java', 'posts': ['post1', 'post2']},
        {'path': '/path/go', 'name': 'go', 'posts': ['post1', 'post3']},
        {'path': '/path/python', 'name': 'python', 'posts': ['post1', 'post2', 'post4']},
    ],
    'categories': [
        {'posts': ['post1', 'post2'], 'path': 'category1.path', 'name': 'category1'},
        {'posts': ['post3', ], 'path': 'category2.path', 'name': 'category2'}
    ]
}

tinysou_search = {
    'enable': True,
    'id': 1,
    }

theme = {
    'toc': {
        'aside': True,
    },
    'author': {
        'tsina': 'sina weibo',
        'weibo_verifier': 'weibo_verifier....',
        'github': 'ideascf',
        'douban': 'wuchong1014',

    },
    'links': {
        'manong': 'https://coderq.com,programmer share...',
        'joychen': 'http://wuchong.me',
    },
}

widgets = [
    'rss',
    'weibo',
]

item = {
    'content': 'item-content',
}

app.jinja_env.globals.update(
    gettext=gettext,
    toc=toc,
    list_archives=list_archives,
    tagcloud=tagcloud,
    date_xml=date_xml,
    root_for=root_for,
    cur_year=cur_year,

    config=config,
    theme=theme,
    site=site,
    tinysou_search=tinysou_search,
    widgets=widgets,

    item=item,
)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
