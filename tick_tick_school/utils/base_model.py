from django.db.models import Model


class Property(Model):
    class Meta:
        abstract = True

    def get_owner_(self):
        pass
