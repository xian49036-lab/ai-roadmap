# ============================================================
# day05 · 文件读写  【B 类 · 半抽象 · 先看视频再动手】
# ============================================================
#
# ⚠️ 今天有一个视频，先看再写。
#
# 【要看的视频】
#   B 站搜索：小甲鱼 零基础入门学习Python  文件
#   或直接搜集名：文件：因为懂你，所以永恒
#   集数：第 28 集（合集 BV1Xv411k7Tp，如链接失效按集名搜）
#   时长：约 17 分钟
#   ★ 看完留 5 分钟：合上视频，用自己的话说一遍"with open 是怎么工作的"
#
#   只看第 28 集就够了。第 29、30 集（文件系统、永久存储）现在不用看。
#
# 今日安排（2.5 小时）：
#   0:00 — 0:10   回顾：字符串的 split / join
#   0:10 — 0:37   看视频 17 分钟 + 理解 5 分钟
#   0:37 — 1:05   把下面三段跑一遍，对照视频里的说法
#   1:05 — 1:55   做练习 3 + 挑战题
#   1:55 — 2:15   复述：为什么要用 with？不用 with 会怎样？
#   2:15 — 2:25   提交
#
# 明天（day06）把 day04 + day05 整合成"成绩单分析器"。
# ============================================================

import os

# 拿到"本文件所在文件夹"的路径，这样从哪个目录运行都能找到数据文件
BASE = os.path.dirname(os.path.abspath(__file__))


# ============================================================
# 五、读文件（with open）
# ============================================================
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

# 三个参数记住：
#   "r"   = 读（默认）
#   encoding="utf-8" = 编码，中文文件必须写，否则可能乱码或报错
#   as f  = 给这个文件起个临时名字，后面用 f 操作它


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
# ⚠️ "w" 会把原文件清空，用它之前先确认没重要内容


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

# 练习 3：读文件统计（不看着上面的代码写，自己重写一遍）
# 要求：读 scores.csv，打印"每个人 姓名 + 总分"，最后打印全班总分
# 提示：with open + readline 跳过表头 + for line in f
print("--- 练习 3 ---")
# 在下面写你的代码


# 挑战题：把练习 3 的结果写进文件
# 要求：生成 report.txt，内容形如：
#   姓名: 小明  总分: 255
#   姓名: 小红  总分: 273
#   姓名: 小刚  总分: 217
#   姓名: 小丽  总分: 185
#   全班总分: 930
# 提示：用 "w" 模式打开，先 open 再 write，最后读回来验证
print()
print("--- 挑战题 ---")
# 在下面写你的代码


# 自测（做完再回答，写在这里）：
#   1. 为什么用 with open 而不是 f = open(...)  + f.close()？
#   2. "w" 和 "a" 的区别是什么？用 "w" 有什么风险？
#   3. 中文文件不加 encoding="utf-8" 可能会怎样？
