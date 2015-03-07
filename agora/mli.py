from mieli import registry
from agora.api import agora_, user

registry.add_hook('user_create', user.create)
registry.add_hook('nexus_create', agora_.create)
