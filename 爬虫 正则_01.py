import re
print(f"第一种")
#findall: 匹配字符串中所有的符合正则表达式的内容

lst = re.findall(r"\d+","我的电话号码是：10086，我女朋友的电话号码是10010")
print(lst)

print(f"第二种")
#*finditer: 匹配字符串中所有的内容，【降负荷的内容返回到迭代器之中】，
# 从迭代器中获取内容需要使用.group()*#

it = re.finditer(r"\d+","我的电话号码是：10086，我女朋友的电话号码是10010")

for i in it:
    print(i.group())

print(f"第三种")

#search,search只要找到一个结果就会返回，返回的结果是match对象，拿数据需要。group()
s = re.search(r"\d+","我的电话号码是：10086，我女朋友的电话号码是10010")
print(s.group())


print(f"第四种")
#match: match会从头开始匹配，相当于^\d+
M= re.match(r"\d+","10086，我女朋友的电话号码是10010")
print(M.group())

print(f"第五种")

#预加载正则表达式
obj = re.compile(r"\d+")  #单独的加载正则表达式的格式

ret = obj.finditer("我的电话号码是：10086，我女朋友的电话号码是10010")
for it in ret:
    print(it.group())

ret = obj.findall("呵呵，我就不行你不还我10000元")
print(ret)


print(f"第六种")


q = """""
    <div> class='jay'><sapan id='1'>郭麒麟</span></div>
    <div> class='jj'><sapan id='1'>二狗</span></div>
    <div> class='july'><sapan id='1'>王五</span></div>
    <div> class='json'><sapan id='1'>小笨猪</span></div>
    """""
ob = re.compile(r"<div> class='.*?><sapan id='.*?>.*?</span></div>",re.S)
#re.S :让.能都来匹配换行符

result = ob.finditer(q)
for it in result:
    print(it.group())

oc = re.compile(r"<div> class='.*?><sapan id='.*?>(?P<mingzi>.*?)</span></div>",re.S)
#(?P<***>): 讲匹配的值全部都放进***组之中，可以单独的从正则匹配的内容之中进一步提取有利内容
result1 = oc.finditer(q)
for iy in result1:
    print(iy.group("mingzi")) #打印"mingzi" 中的值



#python之中的迭代器知识的补充
