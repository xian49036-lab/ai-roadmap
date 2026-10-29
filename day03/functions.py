# ============================================================
# day03：函数（def）
# 用法：先整个跑一遍看输出，再回来看代码，最后做练习
# 跑：python day03/functions.py
# ============================================================

# ============================================================
# 一、为什么需要函数
# ============================================================
print("===== 一、为什么需要函数 =====")

# 假设你要算三个班的平均分。不用函数，你得把同样的逻辑抄三遍：
scores_a = [88, 92, 75, 60]
scores_b = [70, 81, 93]
scores_c = [55, 66]

total_a = 0
for s in scores_a:
    total_a += s
print("A 班平均：", total_a / len(scores_a))

total_b = 0
for s in scores_b:
    total_b += s
print("B 班平均：", total_b / len(scores_b))

total_c = 0
for s in scores_c:
    total_c += s
print("C 班平均：", total_c / len(scores_c))

# 上面这段能跑，但有三个问题：
#   1. 抄了三遍，改一处就要改三处（漏一处就出 bug）
#   2. 变量名 total_a / total_b / total_c 越来越多
#   3. 别人看你的代码，要读三遍才知道你在干嘛

# 用函数：写一次，用三次


def average(scores):
    """算平均分（三个引号包起来的这段叫文档字符串，写给人看的）"""
    total = 0
    for s in scores:
        total += s
    return total / len(scores)


print("--- 换成函数后 ---")
print("A 班平均：", average(scores_a))
print("B 班平均：", average(scores_b))
print("C 班平均：", average(scores_c))

# 一句话：函数 = 给一段代码起个名字，以后喊名字就能用


# ============================================================
# 二、定义与调用
# ============================================================
print()
print("===== 二、定义与调用 =====")


def say_hello():
    print("你好，我是函数里的代码")


# 上面只是"定义"，还没执行。必须"调用"才会跑：
print("准备调用……")
say_hello()          # 加括号 = 调用
say_hello()          # 可以调用任意多次

# 存起来也不执行，只有加 () 才执行
f = say_hello
print("这行只是把函数存进变量 f，没有输出")
f()


# ============================================================
# 三、参数：把数据喂进去
# ============================================================
print()
print("===== 三、参数 =====")


def greet(name):
    print(f"你好，{name}")


greet("小明")
greet("小红")

# 多个参数


def add(a, b):
    return a + b


print("add(3, 5) =", add(3, 5))
print("add(10, 20) =", add(10, 20))

# 参数可以给默认值：调用时不传就用默认的


def greet2(name, greeting="你好"):
    print(f"{greeting}，{name}")


greet2("小明")                    # 用默认的"你好"
greet2("小红", "早上好")           # 传了就用自己的
greet2("小刚", greeting="晚上好")  # 也可以带名字传（关键字参数）


# ============================================================
# 四、return 和 print 不是一回事（最容易搞混的地方）
# ============================================================
print()
print("===== 四、return vs print =====")


# 版本 A：只打印，不返回
def add_print(a, b):
    print("A 的结果：", a + b)


# 版本 B：返回，不打印
def add_return(a, b):
    return a + b


add_print(2, 3)            # 屏幕上能看到 5
x = add_print(2, 3)        # 屏幕上也有 5
print("但 x 是：", x)       # 但 x 是 None！因为它没有 return

y = add_return(2, 3)       # 屏幕上什么都没有
print("y 是：", y)          # 但 y 是 5

# print = 说给人听（只在屏幕上显示一下，说完就没了）
# return = 交给人用（把结果递出来，可以继续参与计算）

# 所以：如果你要"用这个结果"，必须 return
print("add_return(2,3) * 10 =", add_return(2, 3) * 10)   # 能做
# add_print(2,3) * 10                                     # 会报错：None * 10


# ============================================================
# 五、作用域：函数里的变量，外面看不见
# ============================================================
print()
print("===== 五、作用域 =====")


def make_greeting(name):
    message = "你好，" + name      # message 是"局部变量"，只活在函数里
    return message


print(make_greeting("小明"))
# print(message)                   # 取消注释会报 NameError: message is not defined

# 这样设计是为了防止互相干扰：100 个函数里都能叫 total，互不影响


# ============================================================
# 六、把昨天的代码改写成函数（这才是函数真正的用处）
# ============================================================
print()
print("===== 六、重构昨天的代码 =====")


def count_passed(scores):
    """统计及格人数"""
    count = 0
    for s in scores:
        if s >= 60:
            count += 1
    return count


def find_best(students):
    """找出平均分最高的学生（打擂台）"""
    best = students[0]
    for stu in students:
        avg = sum(stu["scores"]) / len(stu["scores"])
        stu["avg"] = avg
        if avg > best["avg"]:
            best = stu
    return best


ex1 = [88, 92, 75, 60, 95, 45, 78]
print("平均：", average(ex1))
print("及格人数：", count_passed(ex1))

students2 = [
    {"name": "小明", "scores": [88, 92, 75]},
    {"name": "小红", "scores": [95, 90, 88]},
    {"name": "小刚", "scores": [72, 65, 80]},
]
top = find_best(students2)
print("最高：", top["name"], top["avg"])

# 注意：昨天的三道练习，现在变成了三个"可以反复调用的工具"
# 换一批数据，改一个参数就行，逻辑一行都不用动 —— 这就是函数的价值


# ============================================================
# 练习区（从这里开始你自己写）
# ============================================================
print()
print("===== 练习 =====")

# 练习 1：写一个函数 min_max(scores)，同时返回最小值和最大值
# 要求：用 for 循环找，不许用 min() / max()
# 提示：return 可以一次返回多个值 —— return 最小值, 最大值
#       接收的时候写  lo, hi = min_max(...)
print("--- 练习 1 ---")
test1 = [88, 92, 75, 60, 95, 45, 78]
# 在下面写你的代码
def min_max(scores):
    hi = scores[0]
    lo = scores[0]
    for t in scores:
        if  t>hi:
            hi=t
        if  t<lo:
            lo=t
    return lo,hi
lo,hi =min_max(test1)
print ("最大值:",hi,"最小值是:",lo)
       
        
        

        


# 练习 2：写一个函数 grade(score)，返回等级字符串
# 规则：>=90 返回 "优秀"；>=80 "良好"；>=60 "及格"；否则 "不及格"
# 然后循环打印 test2 里每个人的等级
print()
print("--- 练习 2 ---")
test2 = [95, 82, 76, 58, 90]
# 在下面写你的代码

test2 = [95, 82, 76, 58, 90]
def grade(score):
    for line,label in [(90,"优秀"),(80,"良好"),(60,"及格")]:
        if score >= line :
           return label
    return "不及格"
for t in test2:
     print(t, "->", grade(t))

# 练习 3：写一个函数 word_count()text，统计一段文字里每个词出现的次数
# 要求：先 text.split() 切成列表，再用字典累加，最后返回那个字典
# 期望：word_count("猫 狗 猫 鸟 猫") 返回 {'猫': 3, '狗': 1, '鸟': 1}
# 提示：字典累加的标准写法是  d[word] = d.get(word, 0) + 1
print()
print("--- 练习 3 ---")
test3 = "猫 狗 猫 鸟 猫"
# 在下面写你的代码
def word_count(text):
    d = {}
    for word in text.split():
        d[word] = d.get(word,0)+1
    return d
print(word_count(test3))

# 挑战题（做完上面三道再看）：
# 写一个函数 report(scores)，直接打印一份完整报告：
#   平均分：xx.xx
#   最高分：xx
#   最低分：xx
#   及格率：xx.x%
# 然后把 test1 传进去，一行搞定所有统计
print()
print("--- 挑战题 ---")
test1 = [88, 92, 75, 60, 95, 45, 78]
def report(scores):
    avg = (sum(scores)/len(scores))  
    passed =len ([s for s in scores if s >= 60])/len(scores)
    print(f"平均分：{avg:.2f}")
    print(f"及格率：{passed * 100:.1f}%")
    print(f"最高分：{max(scores)}")
    print(f"最低分：{min(scores)}")
report(test1)

