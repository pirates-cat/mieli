from importlib import import_module
from django.conf import settings
import imp

__instance = {}

def autodiscover():
    if len(__instance) > 0:
        return
    for app in settings.INSTALLED_APPS:
        # For each app, we need to look for an mieli.py inside that app's
        # package. We can't use os.path here -- recall that modules may be
        # imported different ways (think zip files) -- so we need to get
        # the app's __path__ and look for mieli.py on that path.

        # Step 1: find out the app's __path__ Import errors here will (and
            # should) bubble up, but a missing __path__ (which is legal, but weird)
        # fails silently -- apps that do weird things with __path__ might
        # need to roll their own admin registration.
        try:
            app_path = import_module(app).__path__
        except AttributeError:
            continue

        # Step 2: use imp.find_module to find the app's mieli.py. For some
        # reason imp.find_module raises ImportError if the app can't be found
        # but doesn't actually try to import the module. So skip this app if
        # its mieli.py doesn't exist
        try:
            imp.find_module('mli', app_path)
        except ImportError:
            continue

        # Step 3: import the app's mieli file. If this has errors we want them
        # to bubble up.
        import_module("%s.mli" % app)
    for event in __instance.keys():
        __instance[event] = sorted(__instance[event], key=lambda hook: hook.priority)

# Hooks are functions executed after an event is signaled.
# They are intended to execute additional required actions.
# Any modification on arguments will be ignored.
def add_hook(event, hook, priority=10):
    hook.priority = priority
    if not event in __instance:
        __instance[event] = []
    __instance[event].append(hook)

def signal(event, **kwargs):
    if not event in __instance:
        return
    for hook in __instance[event]:
        # TODO check if module's function is active
        hook(**kwargs)

# Filters are functions executed to allow customization
# of values used later.
# Functions must return **kwargs.
def add_filter(id_, filter_function):
    add_hook('filter_%s' % id_, filter_function)

def apply_filter(id_, **kwargs):
    real_id = 'filter_%s' % id_
    if not real_id in __instance:
        return
    for filter_ in __instance[real_id]:
        # TODO check if module's function is active
        kwargs = filter_(**kwargs)
    return kwargs
