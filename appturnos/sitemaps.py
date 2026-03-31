from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class TurnosStaticSitemap(Sitemap):
    priority = 0.7
    changefreq = "weekly"

    def items(self):
        return [
            "citas",
        ]

    def location(self, item):
        return reverse(item)
