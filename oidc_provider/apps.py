from django.apps import AppConfig


class OIDCProviderConfig(AppConfig):

    name = 'oidc_provider'
    verbose_name = u'OpenID Connect Provider'
    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'oidc_provider',
                'regex': r'^openid/',
                'relative_path': 'oidc_provider.urls',
            }
        }
