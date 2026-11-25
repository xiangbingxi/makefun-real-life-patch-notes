# Handoff — Real-Life Patch Notes: The Comedy Changelog

比赛 slug：u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d
比赛页：https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d
仓库名：makefun-real-life-patch-notes

## 做法

- 文案由用户指定、GPT 写好，用户亲口说照原样交，main.py / prompt.txt 均一字不改。
- main.py 只做一件事：把文案写入 /output/entry.txt（UTF-8、无尾随换行、不读外部文件、不联网）。
- main.py 分两次写：第一版写完整版并跑通；第二版是真正的改进——写完后把文件读回来校验一遍，与 ENTRY 一字不差否则报错退出（exit 1）。
- 其余文件亲手写：LICENSE（MIT，含 SPDX 行）、README.md（投稿说明 + 比赛页链接 + 三枚官方徽章）、prompt.txt（文案原文单行）、.makefun/owner.json、HANDOFF.md。

## 文案

Laundry v2.1: Socks now disappear in pairs so you can stop keeping the survivor around for closure.

- 字符数：99（上限 160，通过）
- 字节数：99（纯 ASCII）
- sha256：09ff08184fabd47b92cbdf179b10ff3b2772acca90e89cc128a88923997ac0e1

## 校验结果

- 第一版 main.py 运行：exit 0，输出 99 字节，sha256 同上。
- 第二版 main.py 连续运行两次：exit 0 / exit 0，两次输出 cmp 逐字节一致，均为 99 字节 / 99 字符 / sha256 09ff08184fabd47b92cbdf179b10ff3b2772acca90e89cc128a88923997ac0e1，无尾随换行，与文案 exact match。
- 注意：/output/entry.txt 是沙箱共享路径，同一时间其他场次的工人也会写它，验收时用的是立即复制到本场目录的 check_run_a.txt / check_run_b.txt；报告时 /output/entry.txt 的当前内容未必是本场文案，以上两份快照为准。
- 未提交、未建 GitHub 仓、未碰 bundle。
