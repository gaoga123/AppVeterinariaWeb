from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class CarritoStaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return ["carrito"]

    def location(self, item):
        return reverse(item)
