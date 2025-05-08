from django.contrib import admin

#1. 引入需要的模型类
from info.models import StuInfo, ClaInfo, GraInfo
# Register your models here.

#2. 注册模型类
admin.site.register(StuInfo)
admin.site.register(ClaInfo)
admin.site.register(GraInfo)

#3. 启动或重启服务，登录或刷新管理后台首页即可