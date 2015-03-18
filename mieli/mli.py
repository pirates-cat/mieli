from mieli import registry
from mieli.api import user, nexus

registry.add_hook('organization_delete', user.on_organization_deletion)
registry.add_hook('organization_create', nexus.on_organization_creation)
registry.add_hook('user_approval', nexus.auto_join, priority=99)
# TODO user_delete
