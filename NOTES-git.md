# Git 复习笔记（2026-10-27）

## 一句话理解

Git = 给代码**拍照存档**。三条命令：`add`（挑出来）→ `commit`（存档）→ `push`（寄到 GitHub）。

---

## 四层结构

| 层 | 是什么 | 用大白话说 | 命令 |
|---|---|---|---|
| 工作区 | 你 D 盘里的文件 | 桌上的**草稿纸** | 你敲代码 |
| 暂存区 | 已 `add` 的内容 | 挑出来**装进信封的那几张** | `git add` |
| 本地仓库 | `.git` 文件夹 | **封口、贴邮戳、存档** | `git commit` |
| 远端仓库 | GitHub 上的副本 | **复印一份寄给公司** | `git push` |

**核心：`commit` 只收信封里的东西，不会自动收走你桌上所有草稿。**

前三步都在本地，只有 `push` 需要网络。

---

## git status 两列怎么读

```
[M ]  README.md
 ↑↑
 │└─ 右列 = 工作区（桌上）的状态
 └── 左列 = 暂存区（信封里）的状态
```

**左列有字母 = 可以提交了；只有右列有字母 = 还没 add。**

完整版 `git status` 不显示列，它用**标题分段**：

| 完整版标题 | 等于 |
|---|---|
| `Changes to be committed:` | 左列有内容 → 该 `commit` |
| `Changes not staged for commit:` | 右列有内容 → 该 `add` |

⚠️ `to be committed` 是**将要**被提交，不是已经提交。
⚠️ `git status` 永远不会提示你 `push` —— 它只管本地。

---

## 状态码对照表

| 显示 | 含义 | 下一步 |
|---|---|---|
| `[??]` | 新文件，git 完全不认识 | `git add` |
| `[ M]` | 改了，没 add | `git add` |
| `[M ]` | 已 add，等着提交 | `git commit` |
| `[MM]` | add 之后又改了 | 再 `git add` 一次 |
| `[A ]` | 新文件已加入 | `git commit` |
| 空白 | 全干净 | 没事干 |

`A` 只会出现在左列（新建文件被加入暂存区）。右列遇到新文件永远是 `??`。

---

## 日常循环（背下来）

```bash
git status                 # 我现在在哪一步？
git add .                  # 放进信封（. 表示所有改动）
git commit -m "说明"        # 存档
git push                   # 寄到 GitHub
```

`git add` 后面必须跟东西，光写 `git add` 会报 `Nothing specified`。

---

## 今天踩的坑

| 坑 | 原因 | 解法 |
|---|---|---|
| `nothing added to commit` | 没 `add` 就 `commit` | 先 `git add .` |
| `Nothing specified, nothing added` | `git add` 没带文件 | `git add .` |
| 改了但 status 没反应 | **没按 Ctrl+S 保存** | 看标题栏有没有 ● 圆点 |
| `Connection was reset` | 命令行不走系统代理 | `git config --global http.proxy http://127.0.0.1:7890` |
| `Repository not found` | 用户名写错 / 仓库没建 | 核对地址栏真实用户名 |
| `rejected` | 建仓库时勾了 README | 建仓库时三个勾选框都不勾 |

---

## 环境备忘

- 仓库：https://github.com/xian49036-lab/ai-roadmap
- 代码目录：`D:\code\day01`
- 代理：FlClash，端口 `7890`（关掉 FlClash 后 push 会失败）
- VS Code 已装中文语言包

---

## 复习自测（不看上文回答）

1. `git add` 之后、`commit` 之前，`git status --short` 左列显示什么？
2. `[MM]` 是什么意思？该做什么？
3. `commit` 完了但没 `push`，别人能在 GitHub 上看到吗？
4. 改了文件但 status 毫无反应，第一个该怀疑什么？
