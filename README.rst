pyramid_braintree
=================

Braintree initializer for the Pyramid Web Framework. 100% Test Covered.

- The following configuration options are required in your config.ini::

    braintree.environment = sandbox
    braintree.merchant_id = MY_MERCHANT_ID
    braintree.public_key = MY_PUBLIC_KEY
    braintree.private_key = 
        cdKU31rhTCDKgI0VYXwLhakDyd0HgR56tDLMRGBIjEdgdshmOLQeXSeohkwppayDPUofhl3
        Vjj01TOwiM29sVYhP22piInAp9jwoDcKenz2rPLvQX4KKSl6SYIGg2jAq1qZPj1AUzdSTya
        6T6j5FDauTSBPoPDghmBAceyt2ZwQW5WVDeLLKyE8ZTn0YVujdKQB5uf2dwk5SlbAZRza3d
        4kBDZEN9uGnKoINPXnFBxkN6OddyY7asUb3sXHIIO0JnsoJd75pvnw9V3I98Uk9k4hPIyvb
        jJIH96lhQWX783be5j1dyQUdDWW3VraWwFIJvED4YoL71OtGEhcG6aOnhkXEqjzmZw4G7km
        jyge5ZyVadc2g8fwlVpWy0dY3bKzvEtkNVVu47Ee0DxmfhFIdi5SepdfCkwnAj8

- The following configuration options are supported for ``environment``:
  
  - ``development``
  - ``production``
  - ``sandbox``

- Additionally, the ``use_unsafe_ssl`` option may be specified (otherwise, this
  configuration wisely defaults to ``False``)::

    braintree.use_unsafe_ssl = True
