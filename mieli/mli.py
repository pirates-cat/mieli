from mieli import registry
from mieli.api import user

registry.register('organization_delete', user.on_organization_deletion)
