from djangoautoconf.auto_conf_admin_utils import register_all_in_module
from external_apps.mail_ticket.mail_ticket import models

__author__ = 'q19420'


register_all_in_module(models)
