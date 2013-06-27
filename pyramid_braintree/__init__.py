import braintree


def string_to_bool(string):
    """ Returns ``True`` if string is "True", otherwise, returns ``False`` """
    return string == 'True'


def includeme(config):
    """ Provide useful configuration to a Pyramid ``Configurator`` instance.

    Currently, this hook will set up and register Braintree.
    The following configurations are required in your configuration file:
        ``braintree.environment``
        ``braintree.merchant_id``
        ``braintree.public_key``
        ``braintree.private_key``

    The following configuration is optional in your configuration file:
        ``braintree.use_unsafe_ssl`` (defaults, wisely, to False)

    Sensible environment options: ``development``, ``production``, ``sandbox``.
    Other configuration data should be copied from your Braintree Sandbox or
    Production account. More at http://braintreepayments.com.
    """

    environment_options = {
        'development': braintree.Environment.Development,
        'production': braintree.Environment.Production,
        'sandbox': braintree.Environment.Sandbox
    }

    settings = config.registry.settings
    settings_env = settings.get('braintree.environment', 'sandbox').strip()

    environment = environment_options[settings_env]
    merchant_id = settings.get('braintree.merchant_id').strip()
    public_key = settings.get('braintree.public_key').strip()
    private_key = settings.get('braintree.private_key').strip()
    use_unsafe_ssl = settings.get('braintree.use_unsafe_ssl', 'False').strip()

    braintree.Configuration.configure(
        environment,
        merchant_id,
        public_key,
        private_key
    )

    braintree.Configuration.use_unsafe_ssl = string_to_bool(use_unsafe_ssl)
