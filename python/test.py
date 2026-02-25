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

# 第一阶段-第二章-06-标识符
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

# 第一阶段-第二章-08-字符串的三种定义
"""
演示字符串的三种定义方式：
- 单引号定义法
- 双引号定义法
- 三引号定义法 
"""

# 单引号定义法，使用单引号进行包围
nama = '黑马程序员'
print(type(nama))
# 双引号定义法
nama = "黑马程序员"
print(type(nama))
# 三引号定义法，写法和多行注释是一样的
"""
我是 
黑马
程序员
"""
print(type(name_))
# 在字符串内 包含双引号
name = "'黑马程序员'"
print(name)
# 在字符串内 包含单引号
name = '"黑马程序员"'
print(name)
# 使用转义字符\解除引号的效用
name = "\"黑马程序员\""
print(name)
name = '\'黑马程序员\''
print(name)
'''
这里\"起到了打断作用，第一个"被正常读取，第二个\"告诉解释器这是一个普通的引号,
于是解释器不会凑齐三个引号
'''
name = """我想打印四个双引号:"\""" """
print(name)
# 用单三引号包围双引号，怎么打都不会报错
name = '''我想打印四个双引号:""""'''
print(name)
# 只要不出现3个连续的双引号就能打印，但是这样加空格看起来比较别扭，可以使用字符串拼接
name = """我想打印四个双引号:"" "" """
print(name)
# 字符串拼接
name = """我想打印四个双引号:"""+'""""'
print(name)
# 第一阶段-第二章-09-字符串的拼接
# 字符串字面量之间的拼接
print("学IT来黑马" + "月薪过万")
# 字符串字面量和字符串变量的拼接
name = "黑马程序员"
address = "建材城东路9号院"
print("我是：" + name + "，我的地址是：" + address)
# 第一阶段-第二章-10-字符串格式化
# 通过占位的形式，完成拼接
name = "黑马程序员"
message = "学IT来：%s" % name
print(message)
# 通过占位的形式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "Python大数据学科，北京%s期，毕业平均工资：%s " % (class_num, avg_salary)
print(message)
# 完成字符串、整数、浮点数，三种不用类型变量的占位
name = "传智播客"
setup_year = 2006
stock_price = 19.99
message = "%s，成立于：%05d，我今天的股价是：%f" % (name, setup_year, stock_price)
print(message)
# 第一阶段-第二章-11-字符串格式化的精度控制
num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.345宽度不限制，小数精度2，结果数：%.2f" % num2)
# 第一阶段-第二章-12-字符串格式化的方式二
"""
演示第二种字符串格式化的方式:f"{占位}"
"""
name = "传智播客"
set_up_year = 2006
stock_price = 19.99
print(f"我是{name}，我成立于：{set_up_year}年，我今天的股价：{stock_price}")
name = "慕岩松"
age = 32
print(f"你好，{name}!你今年{age}岁了。")
print(f"一年以后你将{age+1}岁。")
x = 5
y = 3
print(f"{x}加{y}等于{x+y}")
# 第一阶段-第二章-13-对表达式进行格式化
"""
演示表达式进行字符串格式化
"""
print("1 * 1的结果是：%d" % (1 * 1))
print("1+2和1+3结果分别是：%d和%d" % (1+2, 1+3))
print(f"1 * 1的结果是：{1 * 1}")
print("字符串在Python中的类型名是：%s" % type("字符串"))

# 第一阶段-第二章-14-字符串格式化练习题讲解
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%.1f，经过%d的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor, growth_days,(stock_price * stock_price_daily_growth_factor ** growth_days)))

# 第一阶段-第二章-15-数据输入(input语句)
"""
演示Python的input语句
获取键盘的输入信息
"""
#input()的功能是获取键盘输入的数据
"""
print("请告诉我你是谁？")
name = input()
print("我知道了，你是：%s" % name)
"""
#input()的括号里可直接写提示信息，下面是简化代码
"""
name = input("请你告诉我你是谁？")
print("我知道了，你是：%s" % name)
"""
#无论键盘输入什么类型的数据，获取到的数据永远是字符串类型。按需求将数据类型转换，例如转换为整形int(num)。
"""
num = input("请告诉我你的银行卡密码：")
print("你的银行卡密码类型是：",type(num))
num = int(num)
print("转换之后的数据类型是：",type(num))
"""
"""
user_name = input("用户名")
user_num = input("卡号")
user_num= int(user_num)
print("你好：%s，您是尊贵的：%sVIP用户，欢迎您的光临。user_name和user_num的数据类型是：" % (user_name, user_num),type(user_name),type(user_num))
"""

# 第一阶段-第三章-01-布尔类型和比较运算符
#


