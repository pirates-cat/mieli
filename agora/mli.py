from mieli import registry
from agora.api import agora_, user, link
from agora import cli

registry.add_hook('user_approved', user.create)
registry.add_hook('user_delete', user.delete)
registry.add_hook('organization_init', link.on_organization_creation)
registry.add_hook('nexus_create', agora_.create)
registry.add_hook('user_join', agora_.join)

registry.add_filter('createorganization_cli_options', cli.createorganization_options)
