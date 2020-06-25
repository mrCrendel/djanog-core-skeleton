from django.core.exceptions import ValidationError
from django.db.models import Model


class BaseService:
    model = Model

    @classmethod
    def get_all(cls):
        return cls.model.objects.all()  # returns all instanses

    @classmethod
    def get_single(cls, **kwargs):
        try:
            return cls.model.objects.get(**kwargs)  # returns signle instance by given kwargs
        except cls.model.DoesNotExists:
            """
                Handle exception here
            """
            return None
        except cls.model.MultipleObjectsReturned:
            """
                Handle exception here
            """
            return None
        except cls.model.FieldDoesNotExist:
            """
                Handle exception here
            """
            raise ValidationError(f"given kwargs can't be applied for cls.Model.__class__.__name__")

    @classmethod
    def get_none(cls):
        return cls.model.objects.none()

    @classmethod
    def filter(cls, **kwargs):
        return cls.model.objects.filter(**kwargs)


class SingleBaseService(BaseService):
    singleton_instance_id = 1

    @classmethod
    def get_all(cls):
        cls.get_solo()
        return cls.model.objects.all()

    @classmethod
    def get_solo(cls):
        obj, _ = cls.model.objects.get_or_create(pk=cls.singleton_instance_id)
        return obj
