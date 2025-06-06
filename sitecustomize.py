import anthropic

_original_init = anthropic.Anthropic.__init__

def _patched_init(self, *args, **kwargs):
    """Wrap Anthropic.__init__ to drop deprecated 'proxies' argument."""
    if 'proxies' in kwargs:
        kwargs.pop('proxies')
    return _original_init(self, *args, **kwargs)

anthropic.Anthropic.__init__ = _patched_init
