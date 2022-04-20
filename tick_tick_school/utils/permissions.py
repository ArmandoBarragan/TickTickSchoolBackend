# DRF imports
from rest_framework.permissions import BasePermission
from rest_framework.authtoken.models import Token

# Django imports
from django.shortcuts import get_object_or_404

# Project imports
from tick_tick_school.users.models import User


def get_pk_from_path(path):
    urls = ['subjects', 'users', 'tasks']
    path = path.replace('/', '')
    for url in urls:
        path = path.replace(url, '')
    import pdb; pdb.set_trace()
    return int(path)


class OwnerPermission(BasePermission):
    """ Permission that declares how only the creator of a db register has access to that same register."""

    def has_permission(self, request, view):
        token = request.headers.get('Authorization', None)
        if token:
            token = token.replace('Token ', '')
        else:
            return False

        try:
            user = Token.objects.get(key=token).user
        except Token.DoesNotExist:
            return False

        pk = get_pk_from_path(request.path)
        model = view.serializer_class.Meta.model
        instance = get_object_or_404(model, pk=pk)

        if model == User:
            has_permission = True if instance.pk == user.pk else False
        else:
            has_permission = True if instance.student.pk == user.pk else False

        return has_permission
