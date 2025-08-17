# CS for NCU 项目结构说明

本文档描述了 `cs4ncu` 项目的整体结构与各目录的作用，帮助贡献者和维护者更好地理解项目组织。

## 📁 项目总体结构

```
cs4ncu/
├── 📄 README.md                 # 项目介绍与快速开始指南
├── 📄 STRUCTURE.md              # 本文档 - 项目结构说明
├── 📄 mkdocs.yml                # MkDocs 配置文件
├── 📄 pyproject.toml            # Python 项目配置与依赖管理
├── 📄 uv.lock                   # 依赖版本锁定文件
├── 📄 .gitignore                # Git 忽略文件配置
├── 📄 .python-version           # Python 版本指定
├── 📁 docs/                     # 📚 主要文档内容目录
├── 📁 overrides/                # 🎨 MkDocs 主题自定义
├── 📁 .github/                  # ⚙️ GitHub 工作流与配置
├── 📁 drafts/                   # 📝 草稿文件（开发用）
└── 📁 class0/                   # 🗂️ 历史内容（待整理）
```

## 📚 核心内容目录 (`docs/`)

这是项目的核心，包含所有面向用户的文档内容：

```
docs/
├── 📄 index.md                  # 网站首页
├── 📄 tags.md                   # 标签索引页面
├── 📁 chapters/                 # 主要学习章节
│   ├── 📁 ch1-farewell-to-newbie/   # 第一章：告别电脑小白
│   ├── 📁 ch2-plan-your-future/     # 第二章：规划你的未来
│   ├── 📁 ch3-ncu-learning-guide/   # 第三章：在 NCU 高效学习
│   └── 📁 ch4-hardcore-skills/      # 第四章：硬核技能入门
├── 📁 appendices/               # 昌大专属附录
│   ├── 📄 a1-postgraduate-recommendation.md    # 保研细则解析
│   ├── 📄 a2-postgraduate-entrance-exam.md     # 考研经验分享
│   ├── 📄 a3-major-transfer-guide.md           # 转专业完全指南
│   └── 📄 a4-program-guides.md                 # 各培养方案导读
├── 📁 specials/                # 特色专题内容
│   └── 📁 vscode-the-ultimate-ide/    # VS Code 终极指南
├── 📁 guides/                  # 贡献与开发指南
│   └── 📁 contributing/        # 贡献者指南
├── 📁 assets/                  # 静态资源文件
│   └── 📄 ncuscc-logo.svg      # 项目 Logo
├── 📁 css/                     # 自定义样式文件
│   ├── 📄 extra.css            # 主样式文件
│   ├── 📄 00-variables.css     # CSS 变量定义
│   ├── 📄 01-layout.css        # 布局样式
│   ├── 📄 02-components.css    # 组件样式
│   ├── 📄 03-admonitions.css   # 提示框样式
│   └── 📄 99-fixes.css         # 样式修复
└── 📁 js/                      # 自定义 JavaScript
    └── 📄 custom.js            # 自定义脚本
```

## 🎨 主题自定义 (`overrides/`)

包含 MkDocs Material 主题的自定义内容：

```
overrides/
├── 📄 main.html                # 主模板覆盖
└── 📁 .icons/                  # 自定义图标（如果有）
```

## ⚙️ 开发与配置

### 配置文件说明

- **`mkdocs.yml`**: MkDocs 的核心配置文件，定义网站结构、主题、插件等
- **`pyproject.toml`**: Python 项目配置，包含依赖管理和项目元信息
- **`uv.lock`**: UV 包管理器生成的依赖锁定文件，确保环境一致性
- **`.python-version`**: 指定项目使用的 Python 版本
- **`.gitignore`**: 定义 Git 版本控制忽略的文件和目录

### GitHub 集成 (`.github/`)

包含 GitHub Actions 工作流程和其他 GitHub 特定配置：

```
.github/
├── 📁 workflows/               # GitHub Actions 工作流
│   └── 📄 deploy-docs.yml      # 文档自动部署流程
└── 📁 ISSUE_TEMPLATE/          # Issue 模板（如果有）
```

## 📝 草稿与开发内容

### `drafts/` 目录

包含开发过程中的草稿文件，主要用于：
- 内容构思和初稿
- 开发文档和笔记
- 临时性说明文档

**注意**: 此目录的内容不会被构建到最终网站中。

### `class0/` 目录

包含项目早期版本的内容，主要是：
- 原始的教学材料
- 需要迁移到新结构的内容
- 历史参考文档

**状态**: 待整理，部分内容可能需要迁移到 `docs/chapters/` 中。

## 🚀 构建与部署

### 本地开发

```bash
# 安装依赖
uv sync

# 启动开发服务器
uv run mkdocs serve

# 构建静态站点
uv run mkdocs build
```

### 自动部署

项目配置了 GitHub Actions 自动部署流程：
- 推送到 `main` 分支时自动构建并部署到 GitHub Pages
- 部署地址：https://ncuscc.github.io/cs4ncu/

## 📋 目录管理原则

### 新增内容指南

1. **主要教学内容** → `docs/chapters/` 对应章节
2. **昌大特定信息** → `docs/appendices/`
3. **特色专题** → `docs/specials/`
4. **贡献指南** → `docs/guides/contributing/`
5. **样式修改** → `docs/css/`
6. **静态资源** → `docs/assets/`

### 文件命名规范

- 使用小写字母和连字符分隔
- 目录名使用复数形式（如 `chapters`, `guides`）
- 文件名具有描述性（如 `file-management.md`）
- 按逻辑顺序编号（如 `01-`, `02-`）

### 标签与分类

项目使用标签系统进行内容分类，详见 `docs/tags.md` 和相关的标签规范文档。

---

*本文档会随着项目结构的演进而更新。如有疑问或建议，欢迎提出 Issue 或 Pull Request。*