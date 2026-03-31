from appcarrito.sitemap import CarritoStaticSitemap
from appdegestion.sitemaps import GestionStaticSitemap
from appmascotas.sitemaps import MascotasStaticSitemap
from appresenias.sitemaps import ReseniasStaticSitemap
from appturnos.sitemaps import TurnosStaticSitemap

sitemaps = {
    "carrito": CarritoStaticSitemap,
    "gestion": GestionStaticSitemap,
    "mascotas": MascotasStaticSitemap,
    "resenias": ReseniasStaticSitemap,
    "turnos": TurnosStaticSitemap,
}
