"""
这是一个python入门文件
"""
# 定义整数字面量
666
# 定义浮点字面量
1.22
# 定义字符串字面量
"你好世界"

print("你好世界")

print(666)

print(1.22)

var = 50
print("余额还剩：",var,"元")
var = var - 10
print("消费10元，余额还剩：",var,"元")
var = var - 10
print("消费10元，余额还剩：",var,"元")
var = var + 5
print("提现5元，余额还剩：",var,"元")

#type查看变量类型，在赋予新的变量然后打印
name1 = 5.12
name1_type = type(name1)
name2 = 666
name2_type = type(name2)
name3 = "瑞幸咖啡"
name3_type = type(name3)
print(name1_type)
print(name2_type)
print(name3_type)
#type直接赋值，给予变量，打印变量
name1a = type(5.12)
name2a = type(666)
name3a = type("今天星期六，晚上6：52")
print(name1a)
print(name2a)
print(name3a)
#直接打印变量类型
print(type(5.12))
print(type(666))
print(type("瑞幸咖啡"))

# 第一阶段-第二章-05-数据类型转换
# 将数字类型转换成字符串
num_str = str(11)
print(type(num_str),num_str)

float_str = str(11.345)
print(type(float_str),float_str)
# 将字符串转换成数字
num = int("11")
print(type(num),num)

num2 = float("11.345")
print(type(num2),num2)
# 浮点型转整形，整型转浮点型
num3 = int(11.345)
print(type(num3),num3)

num4 =float(11)
print(type(num4),num4)
'''
错误示例，想要将字符中转换成数字，必须要求字符中内的内容都是数字
num3 = int("黑马程序员")
print(type(num3),num3)
'''

# 第一阶段-第二章-06-标识符f
#规则：内容限定，限定只能使用：中文、英文、数字、下划线，注意：不能以数字开头
# 错误的代码示范：1_name =“张三"
# 错误的代码示范: name_! ="张三"
name_ = "张三"
_name = "张三"
name_1 = "张三"
name1_ =  "张三"
name1 = "张三"
name_name = "张三"
#规则2：大小写敏感
Itheima = "黑马程序员"
itheima = 666
print(Itheima)
print(itheima)
# 规则3:不可以使用关键字
# 错误的示例，使用了关键字：class = 1
# 错误的示例，使用了关键字：def = 1
Class = 1
Def = 1

# 第一阶段-第二章-07-运算符
# 演示python中的各类运算符
print("1 + 1 = ", 1 + 1)
print("2 - 1 = ", 2 - 1)
print("3 * 3 = ", 3 * 3)
print("4 / 2 = ", 4 / 2)
print("11 // 3 = ", 11 // 3)
print("9 % 2 = ", 9 % 2)
print("2 ** 2 = ", 2 ** 2)
# 赋值运算符
num = 1 + 2 * 3
print("1 + 2 * 3 =",num)
# 复合赋值运算符
# +=
num = 1
num += 1 # num = num + 1
print("num += 1:",num)
num -= 1
print("num -= 1:",num)
num *= 4
print("num *= 4:",num)
num /= 2
print("num /= 2:",num)
num = 3
num %= 2 # num = num % 2
print("num %= 2:",num)
num = 3
num **= 3 #num = num ** 3
print("num **= 2:",num)
num = 9
num //= 2
print("num //= 2:",num)


