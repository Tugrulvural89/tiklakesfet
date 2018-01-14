from django.contrib.sitemaps import Sitemap
from messblog.models import Post, Posten

class PostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.yay_tarih


class PostenSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Posten.objects.all()
    def lastmod(self, obj):
        return obj.yay_tarih
