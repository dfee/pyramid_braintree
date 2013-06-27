import unittest

class TestPyramidIntegration(unittest.TestCase):
    def test_add_braintree(self):
        import braintree
        from pyramid import testing

        settings = {
            'braintree.environment': 'sandbox',
            'braintree.merchant_id': 'MY_MERCHANT_ID',
            'braintree.public_key': 'MY_PUBLIC_KEY',
            'braintree.private_key': 'MY_PRIVATE_KEY',
        }

        config = testing.setUp(settings=settings)
        config.include('pyramid_braintree')

        self.assertEqual(braintree.Configuration.environment,
                         braintree.Environment.Sandbox)
        self.assertEqual(braintree.Configuration.merchant_id,
                         settings['braintree.merchant_id'])
        self.assertEqual(braintree.Configuration.public_key,
                         settings['braintree.public_key'])
        self.assertEqual(braintree.Configuration.private_key,
                         settings['braintree.private_key'])
        self.assertFalse(braintree.Configuration.use_unsafe_ssl)
