# English Reading Companion

> 本地优先的英语伴读项目：Work 负责内容生产，Codex 负责技能与代码迭代，本地目录保存全部正式资产，GitHub 仅管理代码类文件。

## 1. 项目目标

通过真实英文故事与短文，长期提升：

- 阅读理解与阅读流畅度
- 英语表达意识与语感
- 对作者叙事方式和思维方式的理解
- 对文化语境与非字面含义的识别

伴读分析采用四层结构：

1. **Story**：先理解故事、人物、事件和情绪变化。
2. **Language**：学习 idioms、meaning chunks、collocations 和 natural expressions。
3. **Thinking**：理解作者如何组织材料、推进叙事和表达观点。
4. **Beyond the Words**：分析暗示、留白、文化语境和字面之外的意义。

## 2. 工作原则

### 2.1 本地文件是唯一事实来源

聊天记录属于工作过程，不作为正式成果。所有确认后的原文、伴读内容、模板、测试结果和版本记录必须保存为本地文件。

### 2.2 Work 与 Codex 共用同一本地目录

- **Work**：读取原文、生成和修订伴读内容、完成内容复盘。
- **Codex**：维护技能、模板、脚本、测试和版本记录。
- 两者不得同时编辑同一个文件。

### 2.3 云端不作为项目同步机制

Web 项目和跨端聊天不作为正式数据来源，也不假设客户端与 Web 自动同步。需要保留的结果必须写入本地目录。

### 2.4 GitHub 只管理代码类资产

技能、脚本、模板、测试定义和工程文档可以进入 Git；伴读原文和伴读成品默认只保存在本地，并通过独立备份机制保护。

## 3. 目录结构

```text
English-Reading-Companion/
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── .gitignore
│
├── content/
│   ├── sources/                  # 英文原文，仅本地保存
│   └── readings/                 # 正式伴读内容，仅本地保存
│
├── skills/
│   ├── english-reading-companion/
│   └── english-reading-ab-workflow/
│
├── templates/                    # 输出模板
├── scripts/                      # 辅助脚本
├── tests/
│   ├── fixtures/                 # 回归测试样本
│   └── regression/               # 回归测试定义
│
└── reports/
    └── regression/               # 回归测试报告
```

## 4. 文件命名规范

### 4.1 原文

```text
content/sources/NNN-english-slug.md
```

示例：

```text
content/sources/001-let-him-go-olivia.md
```

### 4.2 伴读内容

```text
content/readings/NNN-english-slug.md
```

示例：

```text
content/readings/001-let-him-go-olivia.md
```

### 4.3 回归报告

```text
reports/regression/REG-YYYYMMDD-NNN.md
```

示例：

```text
reports/regression/REG-20260729-001.md
```

文件编号一经使用不得重新分配。英文 slug 使用小写字母和连字符。

## 5. 伴读内容元数据

每篇正式伴读文件开头应包含：

```yaml
---
article_id: "001"
source_title: "Let Him Go, Olivia"
companion_title: "在放手之前：一位母亲拒绝接受终点"
skill: "english-reading-companion"
skill_version: "x.y.z"
generated_at: "YYYY-MM-DD"
regression_report: "REG-YYYYMMDD-NNN"
status: "draft | reviewed | final"
---
```

要求：

- `article_id` 与文件名前缀一致。
- 每个技能目录以 `VERSION` 文件记录机器可读版本；该值必须与 `SKILL.md` 和 `agents/openai.yaml` 中显示的版本一致。
- `skill_version` 必须来自实际调用技能的 `VERSION`，不得凭记忆填写。
- 每次伴读调用必须在用户可见输出中显示 `> Skill: english-reading-companion vX.Y.Z`。
- A/B 工作流必须同时显示自身版本和实际调用的伴读技能版本。
- 未执行回归测试时，`regression_report` 填写 `not-run`。
- 正式归档前将 `status` 更新为 `final`。

## 6. 标准工作流

### 6.1 使用 Work 生成伴读

1. 将英文原文保存到 `content/sources/`。
2. 确认文章编号、标题、作者和原文完整性。
3. 使用 `english-reading-companion` 生成伴读内容。
4. 将结果保存到 `content/readings/`，不要只保留在对话中。
5. 检查标题、四层结构、技能版本和元数据。
6. 人工确认后，将状态从 `draft` 更新为 `reviewed` 或 `final`。

### 6.2 使用 Codex 优化技能

1. 修改 `skills/`、`templates/` 或 `scripts/`。
2. 运行现有回归测试。
3. 将报告保存到 `reports/regression/`。
4. 根据测试结果决定是否提升技能版本。
5. 更新 `CHANGELOG.md`。
6. 提交 Git 并推送到 GitHub。

### 6.3 双轨 A/B 评估

`english-reading-ab-workflow` 每次生成三个独立 Markdown 输出：

1. Baseline：不应用伴读技能。
2. Skilled：明确应用当前版本伴读技能。
3. Comparison：基于证据比较两个输出并提出改进候选。

技能改动只有在回归结果可接受后才能成为正式版本。

## 7. Git 与本地内容边界

建议在 `.gitignore` 中加入：

```gitignore
# Local reading assets
content/sources/
content/readings/

# Local generated reports（如报告不进入 Git）
# reports/regression/

# OS and editor files
.DS_Store
*.swp
```

纳入 GitHub 的内容：

- `skills/`
- `templates/`
- `scripts/`
- `tests/`
- `README.md`
- `AGENTS.md`
- `CHANGELOG.md`
- `.gitignore`

默认不上传 GitHub 的内容：

- 受版权保护的伴读原文
- 正式伴读成品
- 临时文件与本地缓存
- 包含个人信息或敏感内容的文件

## 8. 版本管理

技能采用语义化版本：

```text
MAJOR.MINOR.PATCH
```

- `MAJOR`：输出结构或方法发生不兼容变化。
- `MINOR`：新增栏目、分析能力或兼容功能。
- `PATCH`：修正文案、规则或不改变结构的问题。

每次发布至少记录：

- 技能版本号
- 发布日期
- 对应回归报告编号
- 主要变化
- 已知限制

## 9. 备份策略

由于 `content/` 默认不上传 GitHub，必须配置独立备份：

- macOS：Time Machine
- Linux：`rsync`、Restic 或 BorgBackup
- 可选目标：外接硬盘、NAS 或受控私有云盘

最低建议：

- 每日增量备份
- 每周完整校验
- 至少保留一份与主机物理隔离的副本

## 10. 当前项目边界

本项目不依赖 ChatGPT Web 与桌面客户端之间的项目同步。任何未写入本地目录的对话输出，都视为尚未归档的临时结果。
