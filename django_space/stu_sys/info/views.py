from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.

'''
    视图：其实就是Python函数
    视图/函数的两个要求：
        1.视图函数的第一个参数是接收请求，这个请求其实就是HttpRequest的类对象
        2.视图函数必须返回一个响应
'''

#此处希望用户可以通过访问“ip：端口号/index/”来访问该视图/函数
def index(request):

    # return HttpResponse('OK')
    '''
        render(request, template_name, context=None)  渲染模版的函数
        request: 函数参数
        template_name: 模版路径+模版文件名字
        context=数据库查询数据结果:
    '''
    context = {
        'name' : '双12惊喜连连，点击有惊喜！！'
    }
    return render(request, 'info/index.html', context)