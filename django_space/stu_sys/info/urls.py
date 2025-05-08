# 固定写法，相当于在子应用添加组的概念；再由主应用调用即可
from django.urls import path
from info.views import index

urlpatterns = [
    # path(路由名, 视图函数名)
    path('index/', index)
]