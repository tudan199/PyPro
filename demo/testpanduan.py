
# ……………………………………………………………………………………if  else 的用法
# zidian1={}
#     "姓名":"张三",
#     "年龄":"23",
#     "性别":"男"
# }
# if zidian1.get("姓名")=="张":
#     print("张三的年龄",zidian1["年龄"])
# else:
#     print("没有张")
# ……………………………………………………………………………………if elif else 的用法
# zidian1={}
#     "姓名":"张三",
#     "年龄":"23",
#     "性别":"男"
# }
# if zidian1.get("姓名")=="张":
#     print("张三的年龄",zidian1["年龄"])
# elif zidian1.get("年龄")=="25":
#     print("年龄也不是23")
# else:
#     print("没有张")
# ……………………………………………………………………………………if elif elif else 的用法
# zidian1={
#     "姓名":"张三",
#     "年龄":"23",
#     "性别":"男"
# }
# if zidian1.get("姓名")=="张":
#     print("张三的年龄",zidian1["年龄"])
# elif zidian1.get("年龄")=="25":
#     print("年龄也不是23")
# elif zidian1.get("性别")=="女":
#     print("是女的")
# else:
#     print("没有张")
# ……………………………………………………………………………………is 的用法
# if type(11) is int:
#         print("是int类型")
# else:
#         print("不是int")
# ……………………………………………………………………………………将数组里的值根据大小放入两个数组里
# a=[12,33,43,54,65,76,87,87,99,100]
# highlist=[]
# lowlist=[]
# for i in a:
#     if i < 60:
#         lowlist.append(i)
#     else:
#         highlist.append(i)
# print(a)    
# print(highlist)
# print(lowlist)
# ……………………………………………………………………………………使用requests做接口自动化测试
# import requests

# url = "http://127.0.0.1:8080/morning/user/userLogin"

# payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginName\"\r\n\r\n819626117@qq.com\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginPassword\"\r\n\r\ntudan123\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
# headers = {
#     'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
#     'cache-control': "no-cache",
#     'Postman-Token': "af5c83fa-5c63-4f6a-bf30-c70667f1b653"
#     }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)
# …………………………………………………………………………………………使用requests做接口自动化测试(改良)
# import requests

# url = "http://127.0.0.1:8080/morning/user/userLogin"

# payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginName\"\r\n\r\n819626117@qq.com\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginPassword\"\r\n\r\ntudan123\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
# headers = {
#     'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
#     'cache-control': "no-cache",
#     'Postman-Token': "af5c83fa-5c63-4f6a-bf30-c70667f1b653"
#     }

# response = requests.request("POST", url, data=payload, headers=headers)
# zidian=response.json()
# res=zidian.get("success")
# if res==True:
#     print("邮件发送成功测试成功")
# else:
#     print("接口测试失败")
# ……………………………………………………………………………………自动回复机器人
import requests

url = "http://open.turingapi.com/v1/openapi"
headers = {"Content-Type":"application/json;charset=UTF-8"}
data ={
   "input_text":"谢谢",
   "user_info":{"open_id":"cafd0043-440a-4f67-a95a-3c3a27921529"},
   "robot_id":"207157"
}
res = requests.request("post",url,json=data,headers=headers)
# print(res)只会返回状态码
result=res.json().get("result")
datas=result.get("datas")
print(datas)
for i in datas:
    print("机器人说：",i["value"],"\t")