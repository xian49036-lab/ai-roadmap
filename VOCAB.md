# 代码英文词汇表

> 每天新增一组。**不用背，遇到再查**。同一个词见过 3 次自然就记住了。
> 查词：`Ctrl + F` 搜英文。

## 怎么用这份表（自习节奏）

| 阶段 | 做什么 | 时间 |
|---|---|---|
| 每天写代码前 | 扫一眼当天新增的那一组 | 2 分钟 |
| 写代码时 | 卡住了就 `Ctrl + F` 查，**不要猜** | — |
| 每天结束前 | 挑 3 个今天用过的词，合上文件默写中文 | 3 分钟 |
| 每周日 | 只看「二、报错词」那 14 个，自测一遍 | 10 分钟 |

**优先级：报错词 > 通用关键字 > 当天内容的词。** 因为报错信息你每天都会撞见，而项目专用词查一次就够。

## 目录

1. 每份代码都会见到的词
2. **报错信息里的词（最该认识）**
3. day02 · 列表 list
4. day02 · 字典 dict
5. day03 · 函数 def
6. day04 · 字符串与文件
7. day01 · Git 与终端
8. 读报错的三步法
9. 错词本


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

## 五、day03 · 函数 def

| 英文 | 中文 | 说明 |
|---|---|---|
| `def` | 定义（函数） | `def average(scores):` 开头 |
| `function` | 函数 | 一段起了名字的代码 |
| `define` | 定义 | 只是写好，还没执行 |
| `call` / `invoke` | 调用 | 加 `()` 才算调用 |
| `parameter` | 形参 | 定义时括号里的名字 |
| `argument` | 实参 | 调用时真正传进去的值 |
| `default` | 默认值 | `def greet(name, greeting="你好")` |
| `return` | 返回 | 把结果递出来，可继续参与计算 |
| `None` | 空值 | 函数没写 return 时，返回的就是它 |
| `scope` | 作用域 | 变量能生效的范围 |
| `local` | 局部的 | 函数内部定义的变量，外面看不见 |
| `global` | 全局的 | 整个文件都能用的变量 |
| `docstring` | 文档字符串 | 函数下面 `"""这段"""` |
| `positional` | 位置参数 | 按顺序传：`add(3, 5)` |
| `keyword` | 关键字参数 | 带名字传：`add(a=3, b=5)` |
| `refactor` | 重构 | 不改功能，只改结构（比如把代码包成函数） |
| `split` | 切分（字符串） | `"猫 狗".split()` → `['猫', '狗']` |

### 函数相关的报错

| 报错 | 意思 |
|---|---|
| `TypeError: missing 1 required positional argument` | 少传了一个参数 |
| `TypeError: takes 2 positional arguments but 3 were given` | 多传了一个参数 |
| `NameError: name 'xxx' is not defined` | 函数名/变量名拼错，或没定义 |
| `UnboundLocalError` | 在函数里用了外面同名变量，但又给它赋值了 |

---

## 六、day04 · 字符串与文件

| 英文 | 中文 | 说明 |
|---|---|---|
| `string` | 字符串 | 一串文本，用引号包起来 |
| `split` | 切分 | `"a,b".split(",")` → `['a','b']` |
| `join` | 拼接 | `"-".join(['a','b'])` → `"a-b"` |
| `strip` | 去掉两端空白 | 清洗数据第一步，去空格和 `\n` |
| `replace` | 替换 | `"ab".replace("a","x")` |
| `find` | 查找位置 | 找不到返回 `-1` |
| `count` | 计数 | 出现几次 |
| `startswith` / `endswith` | 以…开头 / 结尾 | 返回 True/False |
| `upper` / `lower` | 全大写 / 全小写 | — |
| `format` | 格式化 | f-string 的排版部分 |
| `whitespace` | 空白字符 | 空格、Tab、换行都属于它 |
| `newline` | 换行符 | 写作 `\n` |
| `parse` | 解析 | 把文本拆成结构化数据 |
| `convert` | 转换 | 比如 `int("88")` 转成数字 |

### 文件相关

| 英文 | 中文 | 说明 |
|---|---|---|
| `open` | 打开（文件） | `open(路径, 模式, encoding)` |
| `with` | 上下文语句 | 用完自动关闭文件，不用手动 close |
| `mode` | 模式 | `"r"` 读 / `"w"` 覆盖写 / `"a"` 追加 |
| `read` | 读（全部） | 得到一整个字符串 |
| `readline` | 读一行 | 常用于跳过表头 |
| `readlines` | 读所有行 | 得到字符串列表 |
| `write` | 写 | `f.write("内容")` |
| `encoding` | 编码 | 中文文件务必写 `"utf-8"` |
| `csv` | 逗号分隔值 | `comma-separated values` |
| `header` | 表头 | 第一行，说明每列是什么 |
| `row` | 行 | 一条记录 |
| `column` | 列 | 一个字段 |
| `delimiter` | 分隔符 | CSV 里通常是逗号 |
| `path` | 路径 | 文件在哪 |

### 文件相关的报错

| 报错 | 中文 | 常见原因 |
|---|---|---|
| `FileNotFoundError` | 找不到文件 | 路径写错，或运行目录不对 |
| `UnicodeDecodeError` | 解码错误 | 文件不是 utf-8（Excel 存的 csv 常是 gbk） |
| `PermissionError` | 没有权限 | 文件被别的程序占用（比如正在 Excel 里打开） |

---

## 七、day01 · Git 与终端

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

## 八、读报错的三步法

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

---

## 九、错词本

> 每次背词答错或混淆的词记在这里。复习时**只看这一节**，其他都是查的，这里是背的。

### 2026-10-28（第 1 轮）

| 英文 | 正确含义 | 我答成了 | 一句话纠正 |
|---|---|---|---|
| `Traceback` | 追踪信息（从最下面一行读起） | 回滚 | 回滚是 Git 的 `rollback`/`revert`，跟 Python 报错无关 |
| `expected` | 期望、**本该有** | 丢失 | `expected` = 少了该有的（如 `expected an indented block`） |
| `AttributeError` | 属性错误：对象没有这个属性/方法 | 以为是"列表里没有香蕉这个字符串" | 报错里带引号的那个词（`'apend'`）才是它不认识的名字，通常是拼错了 |
| `ValueError` | 值错误：类型对、值不合法 | `TypeError` | `int("abc")` 是 ValueError；`5 + "abc"` 才是 TypeError |
| `KeyError` | 键错误：字典没这个键 | `AttributeError` | 方括号里写**字符串** → KeyError；用**点号** → AttributeError |
| `missing` / `required` | 缺少 / 必填的 | 未识别、无法读取 | `missing 1 required positional argument` = 缺 1 个必填的位置参数 |

### 这一轮的通关句（下次先默这三条）

1. **点号出问题 → `AttributeError`；方括号里是字符串 → `KeyError`；方括号里是数字 → `IndexError`。**
2. **类型对不上 → `TypeError`；类型对但值不合法 → `ValueError`。**
3. **`expected` = 少了该有的；`unexpected` = 多出来的。**

### 待复查（下次开头先考这 6 个）

`Traceback` `expected` `AttributeError` `ValueError` `KeyError` `missing`
