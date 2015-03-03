from mieli import registry
from mieli.api import user, nexus

registry.register('organization_delete', user.on_organization_deletion)
registry.register('organization_create', nexus.on_organization_creation)
