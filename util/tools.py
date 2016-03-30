# coding=utf-8
import datetime
from collections import defaultdict, Counter

from flask import url_for

from conf import theme, site

# function


def gettext(str):
    return str


def toc(str, config=None):
    return str


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

    def get_parents(category):
        return filter(
            lambda category: len(category),
            sorted(
                filter(
                    lambda category: category['id'] == category['id'],
                    categories
                ),
                key=lambda category: category[orderby],
            )
        )

    def hierarchical_list(level, parent=None):
        """
        :rtype: str
        """
        result = ''

        for i, cat in enumerate(get_parents(parent)):
            child = None
            if not depth or level + 1 < depth:
                child = hierarchical_list(level + 1, cat['_id'])

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

        for i, category in enumerate(get_parents(parent)):
            if i or level:
                result += separator

            result += '<a class="' + className + '-link" href="' + url_for(site.path['category'], category_id=category['name']) + '">'
            result += transform(category['name']) if transform else category['name']

            if showCount:
                result += '<sup>' + str(len(category['posts'])) + '</sup>'

            result += '</a>'

            if  depth and level + 1 < depth:
                result += flat_list(level + 1, category['id'])

        return result

    if style == 'list':
        result += '<ul class="' + className + '-list">' + hierarchical_list(0) + '</ul>'
    else:
        result += flat_list(0)

    return result


def list_archives(page, options):
    options = options if options else {}

    archive_dir = site.archive_dir
    # timezone = site.timezone
    # lang = page.lang or site.lang
    format = options['format']
    type = options.get('type', 'monthly')
    style = options.get('style', 'list')
    show_count = options.get('show_count', True)
    transform = options.get('transform')
    separator = options.get('separator', ', ')
    class_name = options.get('class', 'archive')
    reverse = options.get('reverse', False)

    result = ''

    posts = sorted(
        page['posts'],
        key=lambda post: post['date'],
        reverse=reverse
    )

    if not len(posts):
        return result

    counter = Counter()
    counter.update(post['date'].date() for post in posts)  # 统计各个日期出现的次数
    data = [
        {'name': date.strftime(format), 'year': date.year, 'month': date.month, 'count': count}
        for date, count in counter.iteritems()
    ]

    def link(item):
        url = archive_dir + '/' + str(item['year']) + '/'

        if type == 'monthly':
            url += ('%02d' % item['month'] + '/')

        # return url_for(url)
        return url

    if style == 'list':
        result += '<ul class="' + class_name + '-list">'

        for item in data:
            result += '<li class="' + class_name + '-list-item">'

            result += '<a class="' + class_name + '-list-link" href="' + link(item) + '">'
            result += transform(item['name']) if transform else item['name']
            result += '</a>'

            if show_count:
                result += '<span class="' + class_name + '-list-count">' + str(item['count']) + '</span>'

            result += '</li>'

        result += '</ul>'
    else:
        for i, item in enumerate(data):
            if i:  # 第一个元素不增加分隔符
                result += separator

            result += '<a class="' + class_name + '-link" href="' + link(item) + '">'
            result += transform(item['name']) if transform else item['name']

            if show_count:
                result += '<span class="' + class_name + '-count">' + str(item['count']) + '</span>'

            result += '</a>'

    return result


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
    root = theme.root
    if not path.startswith(root):
        if path[0] == '/':
            path = root[:-1] + path
        else:
            path = root + path

    return path
