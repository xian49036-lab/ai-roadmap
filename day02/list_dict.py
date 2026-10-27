# ============================================================
# day02：列表（list）与字典（dict）
# 用法：先把整个文件跑一遍，看输出；再回到最下面做 3 道练习
# 跑：python list_dict.py
# ============================================================

# ============================================================
# 第一部分：列表 list
# 列表 = 一排有编号的格子，编号从 0 开始
# ============================================================
print("===== 一、列表基础 =====")

fruits = ["苹果", "香蕉", "橘子"]
print("整个列表：", fruits)
print("第 0 个：", fruits[0])      # 苹果
print("最后一个：", fruits[-1])    # 橘子（-1 表示倒数第一）
print("一共几个：", len(fruits))

# 切片：[开始:结束] 含头不含尾
nums = [10, 20, 30, 40, 50]
print("nums[1:3] =", nums[1:3])   # [20, 30] —— 要 1 和 2，不要 3
print("nums[:2]  =", nums[:2])    # 从头到 2（不含）
print("nums[2:]  =", nums[2:])    # 从 2 到最后
print("nums[::-1]=", nums[::-1])  # 倒过来


print()
print("===== 二、增删改 =====")

fruits.append("葡萄")          # 末尾追加
print("append 之后：", fruits)

fruits.insert(1, "西瓜")       # 插到 1 号位置，后面的往后挤
print("insert 之后：", fruits)

fruits[0] = "青苹果"           # 直接改
print("改第 0 个后：", fruits)

fruits.remove("橘子")          # 按值删（只删第一个匹配的）
print("remove 之后：", fruits)

last = fruits.pop()            # 弹出最后一个，并拿到它
print("pop 出来的是：", last)
print("剩下的：", fruits)


print()
print("===== 三、遍历 =====")

# 只要值
for f in fruits:
    print("水果：", f)

# 同时要编号和值（enumerate 很常用）
for i, f in enumerate(fruits):
    print(f"第 {i} 个是 {f}")


print()
print("===== 四、列表的四个常用操作 =====")

scores = [88, 92, 75, 60, 95]
print("最高：", max(scores))
print("最低：", min(scores))
print("总分：", sum(scores))
print("平均：", sum(scores) / len(scores))
print("降序排：", sorted(scores, reverse=True))

# 列表推导式：一行搞定"筛选"
good = [s for s in scores if s >= 90]
print("90 分以上的：", good)


# ============================================================
# 第二部分：字典 dict
# 字典 = 用"名字"取东西，而不是用编号
# 格式：{键: 值, 键: 值}
# ============================================================
print()
print("===== 五、字典基础 =====")

student = {"name": "小明", "age": 20, "major": "人工智能"}
print("整个字典：", student)
print("取 name：", student["name"])

# 取一个不存在的键会报错，用 get 更安全
# print(student["phone"])          # ← 这行会报 KeyError，可以自己试着取消注释
print("取 phone（get）：", student.get("phone", "没有登记"))

student["age"] = 21               # 改
student["city"] = "成都"          # 新增（键不存在就是新增）
print("改和增之后：", student)

del student["major"]              # 删
print("删掉 major：", student)

print("所有键：", list(student.keys()))
print("所有值：", list(student.values()))
print("所有键值对：", list(student.items()))

for k, v in student.items():
    print(f"  {k} = {v}")


# ============================================================
# 第三部分：列表套字典（最重要的形状，以后的 JSON / DataFrame 都长这样）
# ============================================================
print()
print("===== 六、列表套字典 =====")

students = [
    {"name": "小明", "score": 88},
    {"name": "小红", "score": 95},
    {"name": "小刚", "score": 72},
]

for s in students:
    print(f"{s['name']} 考了 {s['score']} 分")

# 找出分数最高的那个：只用你学过的 for + if
best = students[0]
for s in students:
    if s["score"] > best["score"]:
        best = s
print("最高分：", best["name"], best["score"])


# ============================================================
# 练习区（从这里开始你自己写，上面的代码当一个"参考手册"用）
# ============================================================
print()
print("===== 练习 =====")

# 练习 1：算平均分和及格人数
# 要求：用 for 循环算出平均分、统计 >= 60 的人数，打印出来
# 期望输出类似：平均 82.0 分，及格 4 人
print("--- 练习 1 ---")
ex1 = [88, 92, 75, 60, 95, 45, 78]
# 在下面写你的代码（用 for 循环，别用 sum()）


# 练习 2：用字典存成绩，然后逐个打印
# 要求：建一个字典 {"小明": 88, "小红": 95, "小刚": 72}
#       用 for 遍历，打印 "小明 考了 88 分"
print()
print("--- 练习 2 ---")
# 在下面写你的代码


# 练习 3（有点挑战）：找出平均分最高的学生
# 要求：students2 里每人有 3 科成绩，算出每人的平均分，找出平均分最高的人
print()
print("--- 练习 3 ---")
students2 = [
    {"name": "小明", "scores": [88, 92, 75]},
    {"name": "小红", "scores": [95, 90, 88]},
    {"name": "小刚", "scores": [72, 65, 80]},
]
# 提示：先算 avg = sum(s["scores"]) / len(s["scores"])，再比大小
# 在下面写你的代码
