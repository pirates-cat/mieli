from mieli import registry
from identity import helpers

registry.add_filter('registration_form', helpers.set_extra_fields)
registry.add_hook('registration_clean', helpers.clean_extra_fields)
