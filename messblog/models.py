from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

#başlık, tarih,yazar , yayınlanma, yazılma, draft etiket,
#görsel, görsel host edip çekeceğim başka  model
#abonelik

class language(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=250)


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tags', kwargs={'slug': self.slug})


class Categories(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_filter_category(self):
        return self.post_set.filter(categories=categories)

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

class Image(models.Model):
    name = models.CharField(max_length=200)
    height_field = models.IntegerField(blank=True, null=True)
    width_field = models.IntegerField(blank=True, null=True)
    imageforeing = models.ImageField(upload_to='uploads/%Y/%m/%d/',max_length=300)

    def __str__(self):
        return self.name


class Post(models.Model):
    tag = models.ManyToManyField(Tag)
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    yazi1 = models.TextField(blank=True, null=True)
    yazi2 = models.TextField(blank=True, null=True)
    yazi3 = models.TextField(blank=True, null=True)
    yar_tarih = models.DateTimeField(default=timezone.now)
    yay_tarih = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='static/jpeg/', blank=True, null=True)
    image1 = models.ImageField(upload_to='static/jpeg/', blank=True, null=True)
    image2 = models.ImageField(upload_to='static/jpeg/', blank=True, null=True)
    image3 = models.ImageField(upload_to='static/jpeg/', blank=True, null=True)
    urlembed = models.URLField(max_length=100, blank=True, null=True)
    file = models.FileField(upload_to='static/jpeg/', blank=True, null=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=255)


    def yayinla(self):
        self.yay_tarih = timezone.now()
        self.save()

    def __unicode__(self):
        return self.baslik

    def __str__(self):
        return self.baslik

    def get_absolute_url(self):
        return reverse('blog_post_detail', args={'slug': self.slug, 'categories':self.categories})



class Posten(models.Model):
    tag = models.ManyToManyField(Tag)
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    yazi1 = models.TextField(blank=True, null=True)
    yazi2 = models.TextField(blank=True, null=True)
    yazi3 = models.TextField(blank=True, null=True)
    yar_tarih = models.DateTimeField(default=timezone.now)
    yay_tarih = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='static/jpeg/', blank=True, null=True)
    image1 = models.ImageField(upload_to='static/jpeg/', blank=True, null=True)
    image2 = models.ImageField(upload_to='static/jpeg/', blank=True, null=True)
    image3 = models.ImageField(upload_to='static/jpeg/', blank=True, null=True)
    urlembed = models.URLField(max_length=100, blank=True, null=True)
    file = models.FileField(upload_to='static/jpeg/', blank=True, null=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=255)


    def yayinla(self):
        self.yay_tarih = timezone.now()
        self.save()

    def __unicode__(self):
        return self.baslik

    def __str__(self):
        return self.baslik

    def get_absolute_url(self):
        return reverse('blog_post_detail', args={'slug': self.slug, 'categories':self.categories})
