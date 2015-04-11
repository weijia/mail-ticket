# -*- coding: utf-8 -*-
# Create your models here.
from djangoautoconf.model_duplicator import get_duplicated_model
from post_office.models import Email

c = get_duplicated_model(Email, "Email")