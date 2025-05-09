from django.apps import AppConfig


class InfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'info'
    # 后台管理的站点名称
    verbose_name = '学生信息管理'
