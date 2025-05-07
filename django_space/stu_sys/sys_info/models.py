from django.db import models

# Create your models here.


'''
1. 模型类需要继承自models.Model
2. 系统自动为我们创建ID主键
3. 字段定义：
    字段名 = model.类型(选项)
        字段名：数据表中的字段名；字段名不可以使用关键字（python，mysql等）
'''

#班级信息表
class ClaInfo(models.Model):
    name = models.CharField(max_length=10)
    pass

#年级信息表
class GraInfo(models.Model):
    name = models.CharField(max_length=10)
    pass

#学生信息表 必须要继承的对象是models.Model
class StuInfo(models.Model):
    name = models.CharField(max_length=10) # name 为字符串，长度为10
    age = models.IntegerField()
    gender = models.BooleanField()
    is_clainfo = models.ForeignKey(ClaInfo, on_delete=models.CASCADE)
    is_grainfo = models.ForeignKey(GraInfo, on_delete=models.CASCADE)
    pass