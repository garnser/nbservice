import packaging.version as _pv

_orig_Version = _pv.Version

def _patched_Version(v, *args, **kwargs):
    """
    packaging.Version("4.3.4-Docker-3.3.0") → packaging.Version("4.3.4")
    Leaves any “plain” 4.x.y untouched.
    """
    clean = v.split('-', 1)[0]
    return _orig_Version(clean, *args, **kwargs)

_pv.Version = _patched_Version

from netbox.plugins import PluginConfig
from .version import __version__


class NbserviceConfig(PluginConfig):
    name = 'nb_service'
    base_url = 'nb_service'
    verbose_name = 'Service Management'
    description = 'ITSM Service Management'
    version = __version__
    author = 'Renato Almeida de Oliveira Zaroubin'
    author_email = 'renato.almeida.oliveira@gmail.com'
    min_version = "4.2.0"
    max_version = "4.3.99"
    required_settings = []
    default_settings = {
        "top_level_menu": True
    }

    def ready(self):
        from . import signals
        super().ready()


config = NbserviceConfig # noqa
