# 异常处理
# ……………………………………………………………………………………………………异常处理处理取值越界
# a=[2,4,5]
# try:
#     print(a[3])
# except :
#     print("取值出错了")
# ……………………………………………………………………………………………………异常处理处理取值越界finally
# a=[2,4,5]
# try:
#     print(a[3])
# except :
#     print(a[1])
# finally:
#     print("取值出错了")
# ……………………………………………………………………………………………………方法
# def fangfa(a,b):
#     return a+b
# c=fangfa(8,3)
# print(c)
# d=fangfa(c,4)
# print(d)
# ……………………………………………………………………………………………………字符串和其他类型相加
# d=fangfa(1,False)
# print(d)
# e=fangfa(1,True)
# print(e)
# f=fangfa("fd",2)
# # 字符串和int不能相加
# print(f)   
# ……………………………………………………………………………………………………方法设置默认值
# def fangfa(a=4,b=3):
#     return a+b
# print(fangfa(b=1))
# print(fangfa(1))
# print(fangfa(b=1,a=1))
# print(fangfa(a=1))
# ……………………………………………………………………………………………………不需要参数的方法
# def print_hello():
#     return print("hello")
# print_hello()
# ……………………………………………………………………………………………………类
# 定义类
# class phone():
# # 定义成员变量
#     name="小米",
#     size="5.5英寸",
#     price="328492"
# # 定义类的行为（成员方法）（和一般的方法有一点区别）
#     def call(self):
#         print("可以打电话")
#     def message(self):
#         print("可以发信息")
#     def movie(self):
#         print("可以看视频")
# ……………………………………………………………………………………………………实例化对象
# p = phone()
# print(p.name)
# print(p.price)
# print(p.size)
# p.call()
# p.message()
# p.movie()
# ……………………………………………………………………………………………………类的调用
class person():
    name="zhangsan",
    sex="nan",
    age=23,
    money=3429848
    def talk(self,language="你好"):
        print("我能说{}".format(language))
    def run(self):
        print(self.name)
        self.talk()
p =person()
p.talk("中文")
# 可以给方法一个默认值
p.talk()
# 可以调用类本身的成员变量 print(self.name)
p.run()
# 可以调用类本身的成员方法
# ……………………………………………………………………………………………………继承

class son(person):
    name="xzs"
xiaozs=son()
print(xiaozs.name)
print(xiaozs.money)



