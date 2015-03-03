from mieli import registry
from agora.api import user, agora

registry.register('user_create', user.create)
registry.register('nexus_create', agora.create)
