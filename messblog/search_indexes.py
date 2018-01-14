from __future__ import absolute_import, division, print_function, unicode_literals

import datetime
from haystack import indexes
from messblog.models import Post, Posten


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    yazi = indexes.CharField(model_attr='yazi')
    yazi1 = indexes.CharField(model_attr='yazi1')
    yazi3 = indexes.CharField(model_attr='yazi3')
    yazi2 = indexes.CharField(model_attr='yazi2')
    categories = indexes.CharField(model_attr='categories')


    def get_model(self):
        return Post

class PostenIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    yazi = indexes.CharField(model_attr='yazi')
    yazi1 = indexes.CharField(model_attr='yazi1')
    yazi3 = indexes.CharField(model_attr='yazi3')
    yazi2 = indexes.CharField(model_attr='yazi2')
    categories = indexes.CharField(model_attr='categories')


    def get_model(self):
        return Posten
