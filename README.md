# English Reading Companion

> 本地优先的英语伴读项目：按任务区分内容生产与技能维护，本地目录保存正式资产，GitHub 管理工程文件；符合项目授权的新完整伴读另行私密保存到得到大脑。

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

## 当前技能与使用范围

| 技能 | 当前版本 | 用途 |
| --- | --- | --- |
| [english-reading-companion](skills/english-reading-companion/SKILL.md) | 2.8.6 | 完整伴读及方法内聚焦追问 |
| [english-reading-ab-workflow](skills/english-reading-ab-workflow/SKILL.md) | 1.2.1 | 单篇双轨比较或指定样本的跨样本综合 |

完整伴读面向初级学习者，以原文理解为中心，覆盖四层阅读维度，选择 3–5 个高价值表达，并使用有条件的 Simple English 和简短 English Replay。聚焦追问只应用相关解释和检查，不强加完整模板。

只有本项目完整系列稿的生成或修订，才在生成前读取 [项目系列约定](skills/english-reading-companion/references/project-series.md)，确认来源、编号、目标及覆盖授权。普通伴读和 A/B 评估产物不继承 HONY 保存与私密归档要求。遇到未解决的方法问题时，按入口索引读取 [方法参考](skills/english-reading-companion/references/method.md) 的相关章节。

## 2. 工作原则

### 2.1 已持久化资产以本地文件为准

已持久化项目资产的正式状态以本地文件为准；用户当前提供的修订与授权指导本次处理。项目系列新稿通过校验后直接保存为 draft，不必等待首次保存确认。

### 2.2 按任务区分职责

- **内容任务**：读取原文、生成和修订伴读内容、完成内容复盘。
- **工程任务**：维护技能、模板、脚本、测试和版本记录。
- 使用哪个客户端不改变任务边界；多个执行者不得同时编辑同一个文件。

### 2.3 云端不作为项目同步机制

Web 项目和跨端聊天不作为正式数据来源，也不假设客户端与 Web 自动同步。需要保留的结果必须写入本地目录。

### 2.4 GitHub 只管理代码类资产

技能、脚本、模板、测试定义和工程文档可以进入 Git；伴读原文和伴读成品不进入 Git；本地保存、授权私密归档与独立备份分别管理。

## 3. 目录结构

```text
English-Reading-Companion/
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── .gitignore
├── docs/
│   └── inbox-batch-workflow.md # 合集输入与动态规划流程
│
├── content/
│   ├── inbox/                    # 待处理的 Markdown 原文合集
│   ├── sources/                  # 本地权威原文，不进入 Git
│   ├── readings/                 # 本地伴读稿，符合授权时另行私密归档
│   └── processed/                # 已完成处理的 Markdown 原文合集
│
├── skills/
│   ├── english-reading-companion/
│   │   ├── SKILL.md、VERSION、agents/openai.yaml
│   │   └── references/
│   │       ├── project-series.md
│   │       ├── method.md
│   │       └── getnote-delivery.md
│   └── english-reading-ab-workflow/
│
├── tests/
│   └── regression/               # 回归测试定义
│
└── reports/
    ├── regression/               # 历史回归报告
    ├── evaluations/              # 评估记录
    └── proposals/                # 改进提案
```

`content/` 为本地目录，不随克隆下载；`templates/`、`scripts/` 和 `tests/fixtures/` 当前未纳入仓库，按实际需要新增。

## 4. 文件命名规范

### 4.1 原文

```text
content/sources/HONY-NNN-english-slug.md
```

示例：

```text
content/sources/HONY-001-adoption.md
```

### 4.2 伴读内容

```text
content/readings/HONY-NNN-english-slug.md
```

示例：

```text
content/readings/HONY-001-adoption.md
```

### 4.3 回归报告

```text
reports/regression/REG-YYYYMMDD-NNN.md
```

示例：

```text
reports/regression/REG-20260729-001.md
```

新增 HONY 文章使用 `HONY-NNN` 前缀，从 `HONY-001` 起连续编号；在新规则出现前，后续新增文章均使用这一格式。既有纯数字编号文件保留原名且不重新分配。英文 slug 使用小写字母和连字符。

## 5. 伴读内容元数据

每篇项目系列伴读文件开头应包含不显示给读者的元数据注释：

```html
<!--
article_id: "HONY-001"
source_title: "Adoption"
companion_title: "在放手之前：一位母亲拒绝接受终点"
skill: "english-reading-companion"
skill_version: "x.y.z"
generated_at: "YYYY-MM-DD"
regression_report: "not-run"
status: "draft"
-->
```

要求：

- `article_id` 与文件名前缀一致。
- 每个技能目录以 `VERSION` 文件记录机器可读版本；该值必须与 `SKILL.md` 和 `agents/openai.yaml` 中显示的版本一致。
- `skill_version` 必须来自实际调用技能的 `VERSION`，不得凭记忆填写。
- 每次伴读调用必须在标题下方显示 `> Skill: english-reading-companion vX.Y.Z`。
- A/B 工作流必须同时显示自身版本和实际调用的伴读技能版本。
- 未执行回归测试时，`regression_report` 填写 `not-run`。
- 新稿保存和授权私密归档均保持 `draft`；`reviewed`、`final` 的含义及提升授权遵循 [项目规则](AGENTS.md)。私密归档不自动提升稿件状态。

## 6. 标准工作流

### 6.1 合集输入与动态规划

原文可作为一份包含多篇独立文章的 Markdown 合集进入 `content/inbox/`。合集中的篇数是统计口径，不限定实际执行批量；ChatGPT 根据文章边界、文本完整度和目标文件冲突动态规划处理顺序。只有合集中的全部文章均通过逐篇校验，原始合集才可归档到 `content/processed/`。

完整约定见 [合集输入与动态规划流程](docs/inbox-batch-workflow.md)。

### 6.2 生成项目系列伴读

1. 核对当前技能版本，生成前读取项目系列约定，确认权威原文、文章身份、目标路径与覆盖授权；新增原文先保存。
2. 完整阅读目标原文并生成伴读，保存为 `content/readings/` 下的 `draft` 文件。
3. 校验原文一致性、标题、四层内容、表达与复述要求、版本、隐藏元数据及路径。
4. 本地校验通过且 [项目持续授权](AGENTS.md#得到大脑持续授权) 适用时，读取 [得到大脑交付参考](skills/english-reading-companion/references/getnote-delivery.md)，将完全相同的 Markdown 私密保存到唯一可管理的“英语伴读”知识库。
5. 分别报告本地结果与外部结果；外部成功须满足业务成功、非空笔记 ID、匹配标题和真实私密链接。不确定时查询原任务，不重复提交。

已有稿件的覆盖、状态提升和已有外部笔记的修改按具体授权处理；新稿默认保存不新增确认流程。

### 6.3 优化技能

1. 确认修改范围，保留无关改动，按实际变化更新技能及对应版本元数据。
2. 纯文案或流程范围调整做直接检查；结构变化检查契约；阅读方法变化使用代表性文章回归。复用未变化内容已通过的检查。
3. 在 `CHANGELOG.md` 记录实际验证；只有执行文章回归时才生成 `reports/regression/` 报告。
4. 验证通过后，按授权同步安装副本；Git 提交、推送和发布按明确授权执行。

官方技能校验依赖 `PyYAML`，开发依赖列在 `requirements-dev.txt`。本机已有隔离校验入口时直接复用，避免误用缺少依赖的系统 Python。静态契约检查不证明真实读取行为或学习效果，测试范围也不应无故扩展到全部历史伴读。

### 6.4 双轨 A/B 评估

- **单篇比较**：先独立生成并冻结 Baseline，再应用当前伴读技能生成 Skilled，最后形成 Comparison；输出三个独立 Markdown 文件。
- **跨样本综合**：仅使用用户指定的既有比较产物，生成一份 `reports/ab-synthesis/ABS-YYYYMMDD-NNN.md`，伴读版本取自历史样本，工作流版本取自当前技能，不重写旧产物。

A/B 产物不继承项目系列命名与私密归档流程。评估只提供改进证据，不自动授权修改技能；具体执行和证据门槛见 A/B 技能。

## 7. Git 与本地内容边界

当前 `.gitignore` 已忽略整个 `content/`（包括 inbox、sources、readings 和 processed），以及缓存、环境与系统文件。主要边界如下：

```gitignore
# Local reading assets
content/

# OS and editor files
.DS_Store
*.swp
```

允许纳入 GitHub 的工程资产（部分目录按需创建）：

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
- 本次实际验证记录；执行文章回归时附报告编号
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
