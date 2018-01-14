from django.urls import path, re_path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from messblog.sitemaps import PostenSitemap, PostSitemap


sitemaps = {
 'Post' :  PostSitemap,
 'Posten' : PostenSitemap
}

urlpatterns = [
    path(r'', views.post_list, name='post_list'),
    path(r'tr/', views.post_list, name='post_list'),
    path(r'en/', views.post_list_en, name='post_list_en'),
    path('tr/<categories>/<slug:slug>/', views.blog_post_detail, name='blog_post_detail'),
    path('en/<categories>/<slug:slug>/', views.blog_post_detail_en, name='blog_post_detail_en'),
    path('tr/<categories>/', views.categoryviews, name='categoryviews'),
    path('en/<categories>/', views.categoryviews_en, name='categoryviews_en'),
    path(r'robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),

    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
