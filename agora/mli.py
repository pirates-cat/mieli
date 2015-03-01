from mieli import registry
from agora.api import user

registry.register('user_create', user.create)
