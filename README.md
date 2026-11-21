# AI4Math

把一个数学命题写成 Lean 4，在本机拆分引理、构造证明、检查最终定理。遇到尚未解决的问题，保留已证明的结论和下一次可以接手的具体缺口。整个流程可以在普通 Lake 项目中运行。

## 安装与使用

把本仓库下载或克隆为 `ai4math` 文件夹，放到项目的 `.agents/skills/` 下。使用支持 Agent Skills 的客户端打开项目。在 Codex 中可以直接输入：

> 用 $ai4math 证明：对任意自然数 n，重复写 n 个 true 得到的列表长度为 n。先核对形式陈述，再在本机编译并列出最终定理依赖的公理。

运行示例需要 Lean 4、Lake 和 Python 3。首次使用可通过 elan 获取示例锁定的工具链。在本仓库根目录运行：

```sh
python scripts/audit.py examples/demo Demo Demo.result Demo.Target
```

`examples/demo/Demo/Statement.lean` 固定命题，`examples/demo/Demo.lean` 用归纳法完成证明。检查程序会构建该模块，将最终定理的实际类型与固定命题核对，并打印其传递依赖的公理。这个例子只用 Lean 自带的库。

实际研究可使用社区维护的 [Mathlib](https://github.com/leanprover-community/mathlib4)。已有项目沿用自己的 Lean 和 Mathlib 版本；新项目的配置见[本地环境说明](references/setup.md)。

## 工作方式

- 先固定量词、定义域、假设和结论。条件允许时，由独立读者只看形式陈述做回译，再与原题逐项核对。
- 把未证引理写成归约定理的显式前提，检查每条依赖，最后合成原命题的证明。反驳原命题时，检查其否定命题的证明。
- 每轮留下已证结论、失败路线、剩余命题和复验命令，下一次会话可以从具体缺口继续。

[Skill 入口](SKILL.md) · [回译指南](references/readback.md) · [续研记录](references/handoff.md)
