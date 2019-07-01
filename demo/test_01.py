a=[1,3,4]
# print(a[1])
# b={
#     "name":"张三",
#     "性别":"男"
# }
# print(b["name"])
print(a[1])
print (a[2])
try:
    print(a[3])
except:
    print("错误")
try:
    print(b["name"])
except:
    print("代码错误")