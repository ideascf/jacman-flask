# coding=utf-8
import copy
import datetime
from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)


# function
def gettext(str):
    return str


def toc(str, config=None):
    return str


def list_archives(config):
    """
    返回归档文件
    :return:
    """

    return []

def list_categories(page, categories, options):
    """
    返回该文章的所有分类
    :param categories:
    :param options:  {
                'show_count': false,
                'class': 'article-category',
                'style': 'none',
                'separator': '►'}
    :type categories: list
    :type options: dict
    :return:
    :rtype: list
    """

    style = options.get('style', 'list')
    showCount = options.get('showCount', True)
    className = options.get('class') or 'category'
    depth = options.get('depth', 0)
    orderby = options.get('orderby') or 'name'
    order = options.get('order') or 1
    transform = options.get('transform')
    separator = options.get('separator', ', ')
    showCurrent = options.get('show_current', False)
    childrenIndicator = options.get('children_indicator', False)
    result = ''

    def prepare_query(parent):
        query = {}

        if parent:
            query['parent'] = parent
        else:
            query['parent'] = None

        return filter(
            lambda category: len(category),
            sorted(
                filter(
                    lambda category: category['_id'] == parent,
                    categories
                ),
                key=lambda category: category1[orderby],
            )
        )


    def hierarchical_list(level, parent=None):
        """
        :rtype: str
        """
        result = ''

        for i, cat in enumerate(prepare_query(parent)):
            child = None
            if not depth or level + 1 < depth:
                child = hierarchical_list(level+1, cat['_id'])

            isCurrent = False
            if showCurrent and page:
                for j in range(len(categories)):
                    post = cat['posts'][j]
                    if post and post._id == page['id']:
                        isCurrent = True
                        break

            if not isCurrent and page['base']:
                if page['base'].startswith(cat['path']):
                    isCurrent = True

            additionalClassName = ''
            if child and childrenIndicator:
                additionalClassName = ' ' + 'true' if childrenIndicator else 'false'


            result += '<li class="' + className + '-list-item' + additionalClassName + '">'

            result += '<a class="' + className + '-list-link' + (' current' if isCurrent else '') + '" href="' + url_for(cat['path'], category_id=cat['name']) + '">'
            result += transform(cat['name']) if transform else cat['name']
            result += '</a>'

            if showCount:
                result += '<span class="' + className + '-list-count">' + str(len(cat)) + '</span>'

            if child:
                result += '<ul class="' + className + '-list-child">' + child + '</ul>'

            result += '</li>'

        return result


    def flat_list(level, parent=None):
        result = ''

        for i, cat in enumerate(prepare_query(parent)):
            if i or level:
                result += separator

            result += '<a class="' + className + '-link" href="' + url_for(cat['path'], category_id=cat['name']) + '">'
            result += transform(cat['name']) if transform else cat['name']

            if showCount:
                result += '<span class="' + className + '-count">' + str(len(cat)) + '</span>'

            result += '</a>'

            if not depth or level + 1 < depth:
                result += flat_list(level+1, cat['_id'])

        return result

    if style == 'list':
        result += '<ul class="' + className + '-list">' + hierarchical_list(0) + '</ul>'
    else:
        result += flat_list(0)

    return categories

def tagcloud():
    """
    返回标签云
    :return:
    """

    return ''


def date_xml(date):
    """

    :param date:
    :type date: datetime.datetime
    :return:
    :rtype: str
    """

    return date.strftime('%Y-%m-%dT%H:%M:%SZ')

def open_graph(data):
    return ''

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

def is_post(page):

    return page.get('layout', '') == 'post'


def root_for(path):
    """

    :param path:
    :type path: str
    :return:
    :rtype: str
    """

    path = path if path else '/'
    root = theme['root']
    if not path.startswith(root):
        if path[0] == '/':
            path = root[:-1] + path
        else:
            path = root + path

    return path

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


tag1 = {'path': '/path/java', 'name': 'java', 'posts': ['post1', 'post2']}
tag2 = {'path': '/path/go', 'name': 'go', 'posts': ['post1', 'post3']}
tag3 = {'path': '/path/python', 'name': 'python', 'posts': ['post1', 'post2', 'post4']}

category1 = {'_id': 1, 'posts': ['post1', 'post2'], 'path': 'category', 'name': 'category1', 'parent': None}
category2 = {'_id': 2, 'posts': ['post3', ], 'path': 'category', 'name': 'category2', 'parent': None}

site = {
    'tags': [tag1, tag2, tag3],
    'categories': [category1, category2]
}

menu = [
    {'title': 'home', 'path': '/'},
    {'title': 'categories', 'path': 'categories'},
    {'title': 'archives', 'path': 'archives'},
    {'title': 'tags', 'path': 'tags'},
    {'title': 'about', 'path': 'about'},
]
tinysou_search = {
    'enable': True,
    'id': 1,
    }

theme = {
    'title': "joychen's blog",
    'menu': menu,  # 标题栏菜单
    # 文章目录控制
    'toc': {
        'article': True,
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
    'root': 'http://localhost:8888/',
    'index': {
        'expand': True,
        'excerpt_link': 'Read More',
    },
    'date_format': '%Y-%m-%d',
    'imglogo': {
        'enable': True,
        'src': 'static/img/logo.png'
    },

    'show_article_desc': True,

    'google_analytics': {
        'enable': False,
        'id': '',
        'site': ''
    },
    'baidu_tongji': {
        'enable': False,
        'sitecode': '',
    },
    'cnzz_tongji': {
        'enable': False,
        'siteid': ''
    },


    'google_cse': {
        'enable': False,
        'cx': '',
    },
    'baidu_search': {
        'enable': False,
        'id': '',
        'site': '',
    },
    'tinysou_search': {
        'enable': False,
        'id': '',
    },

    # 'widgets': ['github-card', 'category', 'tag', 'link', 'douban', 'rss', 'weibo'],
    'widgets': ['github-card', 'rss', ],
}

item = {
    'content': 'item-content',
}

article_left = {
    'title': 'title-right',  # 标题
    'date': datetime.datetime.now(),  # 创建日期
    'updated': datetime.datetime.now(),  # 修改日期
    'toc': True, #  是否显示目录
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
    'toc': True, #  是否显示目录
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
    'toc': True, #  是否显示目录
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
    'toc': True, #  是否显示目录
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
    'posts': [article_page,article_page,article_page,article_page,article_page,article_page,],
    'prev_link': '',
    'next_link': '',
    'path': '/',
    'list_number': False,
}

archive_page = {
    'archive': True,
    'year': 2016,
    'month': 12,
    'posts': [article_page,]
}

category_page = {
    'category': 'category1',
}

tag_page = {
    'tag': 'tag1',
}

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
