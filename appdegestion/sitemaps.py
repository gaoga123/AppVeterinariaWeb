from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class GestionStaticSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return ["index", "privacidad", "terminos"]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == "index":
            return 1.0
        return 0.3

    def changefreq(self, item):
        if item == "index":
            return "weekly"
        return "yearly"
