from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class ReseniasStaticSitemap(Sitemap):
    priority = 0.7
    changefreq = "weekly"

    def items(self):
        return [
            "resenias",
        ]

    def location(self, item):
        return reverse(item)
