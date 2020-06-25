from .models import User
from apps.commons.services import BaseService


class UserService(BaseService):
    model = User