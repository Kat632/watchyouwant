"""
Without this line django wouldn't know about
the custom ready method, so the signals
wouldn't work.
"""
default_app_config = 'checkout.apps.CheckoutConfig'
