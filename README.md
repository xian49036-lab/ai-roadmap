# ai-roadmap

20 个月 AI 学习记录。目标：2028 年毕业时进入 AI 行业，月薪 8000+。

主攻方向：AI 应用开发（RAG / Agent / 模型部署），不碰算法研发岗。

## 学习进度

| 日期         | 内容                                       | 产出               |
| ---------- | ---------------------------------------- | ---------------- |
| 2026-10-24 | 环境搭建（Python / VS Code / Git）、Python 基础语法 | `for循环.py` 九九乘法表 |
| 2026-10-27 | Git 首次提交与推送到 GitHub                      | 本仓库跑通            |
| 2026-10-28 | 列表与字典（索引、切片、增删改、遍历、列表套字典）                | `day02/list_dict.py` + `VOCAB.md` |
| 2026-10-29 | 函数：定义、参数、return vs print、作用域、重构          | `day03/functions.py`，错词本已建 |

## 目录结构

```
ai-roadmap/
├── VOCAB.md   代码英文词汇表 + 错词本
├── day01/     Python 基础 + Git
├── day02/     列表与字典
├── day03/     函数
└── day04/     字符串与文件读写（含示例数据 scores.csv）
```

| 路径                 | 内容                                                    |
| ------------------ | ----------------------------------------------------- |
| `VOCAB.md`         | 按天分组的代码英文词汇 + 报错词辨析 + 个人错词本                            |
| `day01/for循环.py`   | 九九乘法表：双层 for 循环 + f-string + `end="\t"` 对齐            |
| `day01/ladder.py`  | Python 入门七关阶梯：print → 变量 → 数据类型 → 输入 → 判断 → 循环 → 嵌套循环 |
| `day01/NOTES-git.md` | Git 复习笔记：四层结构、status 两列、状态码对照、踩坑记录                   |
| `day02/list_dict.py` | 列表与字典：索引切片、增删改、遍历、列表套字典，含 3 道练习                    |
| `day03/functions.py` | 函数：为什么需要函数、参数、return vs print、作用域、重构昨日代码，含 3 道练习 + 1 挑战 |
| `day04/strings_files.py` | 字符串方法、split/join、f-string 排版、文件读写、手写 CSV 统计，含 3 道练习 + 1 挑战 |

## 踩过的坑

- `git commit` 前必须先 `git add`，否则报 `nothing added to commit`
- `git add` 后面必须跟东西（`git add .`），光写 `git add` 报 `Nothing specified`
- 命令行（git / curl）不会自动走系统代理，需要单独配置：`git config --global http.proxy http://127.0.0.1:7890`
- GitHub 上"授权成功"不等于推送完成，还要执行 `git push`
- `commit` 完看到 `ahead 1`，就是忘了 push
- 函数里误用全局变量（`sum(test1)` 而不是 `sum(scores)`），会让函数失去通用性
- 函数只 `print` 不 `return`，外面拿到的就是 `None`

## 下一步

- [x] 列表与字典
- [x] 函数
- [x] 字符串与文件读写
- [ ] 模块与异常处理
- [ ] pandas 数据处理
