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
    return int(path)


class OwnerPermission(BasePermission):
    def has_permission(self, request, view):
        token = request.headers['Authorization'].replace('Token: ', '')
        if token:
            user = Token.objects.get(key=token).user
            pk = get_pk_from_path(request.path)
            model = view.serializer_class.Meta.model
            instance = get_object_or_404(model, pk=pk)
            import pdb; pdb.set_trace()

            if model == User:
                permission = True if instance.pk == user.pk else False
            else:
                permission = True if instance.student.pk == user.pk else False

            return permission
