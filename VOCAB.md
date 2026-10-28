# 代码英文词汇表

> 每天新增一组。**不用背，遇到再查**。同一个词见过 3 次自然就记住了。
> 用法：写代码时卡在某个英文词上，`Ctrl + F` 在这里搜。

---

## 一、每份代码都会见到的词

| 英文 | 中文 | 出现在哪 |
|---|---|---|
| `print` | 打印 / 输出 | `print("你好")` |
| `input` | 输入 | `input("请输入：")` |
| `type` | 类型 | `type(x)` 看它是什么类型 |
| `int` | 整数 | `int("5")` 转成整数 |
| `float` | 浮点数（小数） | `float("3.14")` |
| `str` | 字符串（文本） | `str(123)` 转成文本 |
| `bool` | 布尔（真/假） | `True` / `False` |
| `None` | 空值（什么都没有） | 表示"还没赋值" |
| `for` | 循环：对每个… | `for x in 列表:` |
| `in` | 在…里面 | `if "a" in 列表:` |
| `if` / `elif` / `else` | 如果 / 否则如果 / 否则 | 判断分支 |
| `while` | 当…的时候（循环） | `while x < 10:` |
| `def` | 定义（函数） | `def 函数名():` |
| `return` | 返回 | `return 结果` |
| `True` / `False` | 真 / 假 | 注意首字母大写 |
| `import` | 导入（别人的代码） | `import pandas` |

---

## 二、报错信息里的词（**最该认识的一类**）

| 英文 | 中文 | 说明 |
|---|---|---|
| `Error` | 错误 | 报错开头 |
| `Traceback` | 追踪信息 | 报错时那一大段，**从最下面一行读起** |
| `line` | 行 | `line 12` = 第 12 行出错 |
| `expected` | 期望（你少写了什么） | `expected an indented block` = 期望一个缩进块 |
| `invalid` | 无效的 | `invalid syntax` = 语法无效 |
| `missing` | 缺少 | `missing 1 required argument` = 缺一个必填参数 |
| `not defined` | 未定义 | 变量名拼错，或还没赋值 |
| `IndexError` | 索引错误 | 列表没那么多元素，你却取了第 100 个 |
| `KeyError` | 键错误 | 字典里没有这个键 |
| `TypeError` | 类型错误 | 数字和文字相加了 |
| `ValueError` | 值错误 | 类型对但值不对，如 `int("abc")` |
| `AttributeError` | 属性错误 | 这个对象没有这个方法，如 `列表.apend()` 拼错 |
| `NameError` | 名字错误 | 用了不存在的变量名 |
| `IndentationError` | 缩进错误 | 空格和 Tab 混用了 |

---

## 三、day02 · 列表 list

| 英文 | 中文 | 例子 |
|---|---|---|
| `list` | 列表 | `[1, 2, 3]` |
| `index` | 索引（第几个） | `fruits[0]` |
| `slice` | 切片 | `nums[1:3]` 取第 1 到 2 个 |
| `append` | 追加（到末尾） | `fruits.append("葡萄")` |
| `insert` | 插入（到指定位置） | `fruits.insert(1, "西瓜")` |
| `remove` | 移除（按值） | `fruits.remove("橘子")` |
| `pop` | 弹出（拿掉并取出） | `last = fruits.pop()` |
| `extend` | 扩展（把另一个列表接上） | `a.extend(b)` |
| `sort` | 排序（改自己） | `nums.sort()` |
| `sorted` | 排序（返回新的） | `sorted(nums, reverse=True)` |
| `reverse` | 反转 / 倒序 | `reverse=True` |
| `len` | 长度（有几个） | `len(fruits)` |
| `max` / `min` | 最大 / 最小 | `max(scores)` |
| `sum` | 求和 | `sum(scores)` |
| `range` | 范围 | `range(1, 6)` → 1,2,3,4,5 |
| `enumerate` | 枚举（同时给编号和值） | `for i, f in enumerate(fruits)` |

---

## 四、day02 · 字典 dict

| 英文 | 中文 | 说明 |
|---|---|---|
| `dict` | 字典 | `{"name": "小明"}` |
| `key` | 键（名字） | 冒号左边 |
| `value` | 值 | 冒号右边 |
| `item` | 条目（一对键值） | `items()` 取出所有对 |
| `keys` | 所有键 | `student.keys()` |
| `values` | 所有值 | `student.values()` |
| `get` | 取值（取不到给默认值） | `student.get("phone", "无")` |
| `nested` | 嵌套 | 列表里套字典 |
| `iterate` | 遍历 | 一个个过一遍 |

---

## 五、day01 · Git 与终端

| 英文 | 中文 | 说明 |
|---|---|---|
| `repository` / `repo` | 仓库 | 装代码的地方 |
| `remote` | 远程（的仓库） | GitHub 上那份 |
| `origin` | 源的默认名字 | `origin` 就指你的 GitHub 仓库 |
| `branch` | 分支 | 默认 `main` |
| `stage` / `staged` | 暂存 / 已暂存 | 放进"信封"了 |
| `unstaged` | 未暂存 | 还在"桌上" |
| `untracked` | 未跟踪 | git 还不认识它（`??`） |
| `modified` | 已修改 | 改了但没 add |
| `commit` | 提交（存档） | 一次快照 |
| `message` | 提交说明 | `-m "说明"` |
| `working tree` | 工作区 | 你正在编辑的文件 |
| `clean` | 干净 | 没有未提交的改动 |
| `push` / `pull` | 推送 / 拉取 | 与远端同步 |
| `log` | 日志（提交历史） | `git log --oneline` |

---

## 六、读报错的三步法

1. **只看最后一行**，那里写着错误类型（如 `KeyError`）
2. 往上找 **`line N`**，那就是出错的行号
3. 在本文档搜那个错误类型的中文，就知道大概是哪类问题

例：
```
Traceback (most recent call last):
  File "day02/list_dict.py", line 42, in <module>
    print(student["phone"])
KeyError: 'phone'
```
→ 读作：第 42 行，`KeyError`（键错误），字典里没有 `phone` 这个键。
