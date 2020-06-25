import os
import re
import uuid
from urllib.parse import urlparse, parse_qs

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


def slugify_camelcase(string: str, sep: str = "-") -> str:
    """
    Converts camelcase string to lowercase string divided with given
    separator

    :param string: string to slugify
    :param sep: separator
    :return: slugified string

    With sep='_':
        'CamelCase' -> 'camel_case'
    """
    repl = r"\1{}\2".format(sep)
    s1 = re.sub("(.)([A-Z][a-z]+)", repl, string)
    return re.sub("([a-z0-9])([A-Z])", repl, s1).lower()


def generate_filename(instance, filename: str) -> str:
    """
    Generates a filename for a model's instance

    :param instance: Django model's instance
    :param filename: filename
    :return: generated filename

    Filename consist of slugified model name, current datetime and time
    and uuid
    """
    f, ext = os.path.splitext(filename)
    model_name = slugify_camelcase(instance._meta.model.__name__, "_")
    strftime = timezone.datetime.now().strftime("%Y/%m/%d")
    hex_ = uuid.uuid4().hex
    # return f"{model_name}/{strftime}/{hex_}{ext}"
    return "{}/{}/{}{}".format(model_name, strftime, hex_, ext)


def video_id(value):
    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    query = urlparse(value)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    # fail?
    return None
