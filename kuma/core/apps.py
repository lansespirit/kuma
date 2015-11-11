import jingo
import jingo.monkey
from django.apps import AppConfig
from django.conf import settings
from django.utils import translation
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _


class CoreConfig(AppConfig):
    """
    The Django App Config class to store information about the core app
    and do startup time things.
    """
    name = 'kuma.core'
    verbose_name = _('Core')

    def ready(self):
        super(CoreConfig, self).ready()

        jingo.monkey.patch()
        jingo.env.install_gettext_translations(translation, newstyle=True)

    @cached_property
    def language_mapping(self):
        """
        a static mapping of lower case language names and their native names
        """
        from product_details import product_details
        return dict([(lang.lower(), product_details.languages[lang]['native'])
                     for lang in settings.MDN_LANGUAGES])
