pyramid_braintree
=================

Braintree initializer for the Pyramid Web Framework. 100% Test Covered.

- The following configuration options are required in your config.ini::

    pyramid.includes =
        pyramid_braintree

    braintree.environment = sandbox
    braintree.merchant_id = MY_MERCHANT_ID
    braintree.public_key = MY_PUBLIC_KEY
    braintree.private_key = MY_PRIVATE_KEY

- The following configuration options are supported for ``environment``:
  
  - ``development``
  - ``production``
  - ``sandbox``

- Additionally, the ``use_unsafe_ssl`` option may be specified (otherwise, this
  configuration wisely defaults to ``False``)::

    braintree.use_unsafe_ssl = True
