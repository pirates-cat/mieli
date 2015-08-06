from mieli import registry
from geo import helpers, cli

registry.add_filter('createuser_cli_options', cli.createuser_options)
registry.add_filter('registration_form', helpers.set_extra_fields)
registry.add_hook('registration_clean', helpers.clean_extra_fields)
registry.add_hook('user_create', helpers.on_user_creation)
