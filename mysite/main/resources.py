from import_export import resources
from .models import UserResponse

class UserResource(resources.ModelResource):
    class Meta:
        model = UserResponse
