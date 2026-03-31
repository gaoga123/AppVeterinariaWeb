from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class MascotasStaticSitemap(Sitemap):
    priority = 0.7
    changefreq = "weekly"

    def items(self):
        return [
            "opciones_mascotas",
            "mascotas",
        ]

    def location(self, item):
        return reverse(item)
