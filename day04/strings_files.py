# ============================================================
# day04：字符串处理 + 文件读写
# 用法：先整段跑一遍看输出，再回来看代码，最后做练习
# 跑：python day04/strings_files.py
# ============================================================

import os

# 拿到"本文件所在文件夹"的路径，这样从哪个目录运行都能找到数据文件
BASE = os.path.dirname(os.path.abspath(__file__))


# ============================================================
# 一、字符串也能切片、也能循环
# ============================================================
print("===== 一、字符串基础 =====")

s = "Hello, Python"
print("原字符串：", s)
print("第 0 个字符：", s[0])
print("最后一个：", s[-1])
print("前 5 个：", s[:5])
print("从第 7 个到最后：", s[7:])
print("长度：", len(s))

for ch in "abc":
    print("字符：", ch)


# ============================================================
# 二、最常用的 6 个字符串方法
# ============================================================
print()
print("===== 二、常用方法 =====")

raw = "  小明，88分  "
print("原样：       [", raw, "]")
print("strip()：    [", raw.strip(), "]")            # 去掉两端空白
print("upper()：", raw.strip().upper())              # 全大写
print("lower()：", "Hello".lower())                  # 全小写
print("replace()：", raw.replace("88", "95"))        # 替换
print("find()：", raw.find("88"))                    # 找到的位置，找不到返回 -1
print("count()：", raw.count("8"))                   # 出现几次
print("startswith()：", "小明".startswith("小"))      # 是不是以…开头

# 注意：这些方法都**不会改动原字符串**，而是返回一个新的
print("raw 变了吗？没有：", raw)


# ============================================================
# 三、split 和 join（处理数据最重要的两个）
# ============================================================
print()
print("===== 三、split 和 join =====")

line = "小明,88,92,75"
parts = line.split(",")          # 按逗号切开 → 列表
print("split 结果：", parts)
print("第 1 个字段：", parts[0])
print("第 2 个字段（还是字符串）：", parts[1], type(parts[1]))

# 想要数字，必须自己转
print("转成整数后 +10：", int(parts[1]) + 10)

# join：把一个列表拼成字符串
words = ["我", "喜欢", "Python"]
print("用空格拼：", " ".join(words))
print("用横线拼：", "-".join(words))

# 经典组合：先把逗号换成空格，再切开
print("'a,b,c' 切成列表：", "a,b,c".split(","))
print("再拼回去：", " / ".join("a,b,c".split(",")))


# ============================================================
# 四、f-string 进阶：对齐和补零
# ============================================================
print()
print("===== 四、f-string 排版 =====")

rows = [("小明", 88), ("小红", 100), ("小刚", 7)]
for name, score in rows:
    # <8 表示占 8 位、左对齐；>5 表示占 5 位、右对齐
    print(f"{name:<8}\t{score:>5}")

print(f"补零：{7:03d}")        # 007
print(f"保留两位：{3.14159:.2f}")


# ============================================================
# 五、读文件（with open）
# ============================================================
print()
print("===== 五、读文件 =====")

path = os.path.join(BASE, "scores.csv")
print("正在读：", path)

# with 的意思是"用完自动关掉文件"，不用手动 close
with open(path, "r", encoding="utf-8") as f:
    content = f.read()          # read() 一次读全部，得到一个字符串
print("--- read() 读到的原始内容 ---")
print(content)

# 逐行读更常用：for line in f
with open(path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i >= 3:              # 只看前 3 行
            break
        print("第", i, "行：", repr(line))   # repr 能看到 \n


# ============================================================
# 六、写文件
# ============================================================
print()
print("===== 六、写文件 =====")

out_path = os.path.join(BASE, "demo_output.txt")

# "w" = 覆盖写入（原来的内容没了）
with open(out_path, "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")

# "a" = 追加（接在后面写）
with open(out_path, "a", encoding="utf-8") as f:
    f.write("追加的一行\n")

with open(out_path, "r", encoding="utf-8") as f:
    print("--- 写完之后读回来 ---")
    print(f.read())

# 三种模式记住：
#   "r" 读（默认）  "w" 覆盖写  "a" 追加写


# ============================================================
# 七、实战：读 CSV 做统计（这就是 pandas 替你做掉的事）
# ============================================================
print()
print("===== 七、读 CSV 做统计 =====")

students = []

with open(path, "r", encoding="utf-8") as f:
    header = f.readline()               # 第一行是表头，先读掉
    header = header.strip().split(",")
    print("表头：", header)

    for line in f:                      # 剩下的每一行
        line = line.strip()             # 去掉行尾的 \n
        if not line:                    # 空行跳过
            continue
        parts = line.split(",")
        name = parts[0]
        scores = [int(parts[1]), int(parts[2]), int(parts[3])]
        students.append({
            "name": name,
            "scores": scores,
            "total": sum(scores),
            "avg": sum(scores) / len(scores),
        })

# 打印成一张表
print()
print(f"{'姓名':<6}{'总分':>6}{'平均':>8}")
print("-" * 22)
for s in students:
    print(f"{s['name']:<6}{s['total']:>6}{s['avg']:>8.1f}")

# 找出总分最高的（复用 day02 的打擂台）
best = students[0]
for s in students:
    if s["total"] > best["total"]:
        best = s
print()
print("总分最高：", best["name"], best["total"])


# ============================================================
# 练习区（从这里开始你自己写）
# ============================================================
print()
print("===== 练习 =====")

# 练习 1：清洗一批脏字符串
# 要求：去掉每项两端的空格和换行，丢弃空字符串，结果放进新列表并打印
print("--- 练习 1 ---")
dirty = ["  小明 ", "小红\n", "", " 小刚  ", "\n", " 小丽"]
# 在下面写你的代码


# 练习 2：路径转换
# 要求：把 "a-b-c-d" 转成 "a/b/c/d"，再转成 "a -> b -> c -> d"
# 只能用 split 和 join，不许用 replace
print()
print("--- 练习 2 ---")
raw2 = "a-b-c-d"
# 在下面写你的代码


# 练习 3：读文件统计（不看着上面的代码写，自己重写一遍）
# 要求：读 scores.csv，打印"每个人 姓名 + 总分"，最后打印全班总分
print()
print("--- 练习 3 ---")
# 在下面写你的代码（提示：with open + readline 跳过表头 + for line in f）


# 挑战题：把练习 3 的结果写进文件
# 要求：生成 day04/report.txt，内容形如：
#   姓名: 小明  总分: 255
#   姓名: 小红  总分: 273
#   ...
#   全班总分: xxx
# 提示：用 "w" 模式打开，先 open 再 write，最后读回来验证
print()
print("--- 挑战题 ---")
