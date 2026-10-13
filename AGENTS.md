# AGENTS.md · ai-governance-checklist

> 机器可发现入口（AI 编码代理 / Codex / Claude / Cursor）。单一事实源：本文件。

## 这是什么
医疗 AI 治理的聚合开源仓：模型卡 / 数据卡模板 + 人类监督（human-in-the-loop）检查单 + 公平性测试骨架 + OWASP AI Exchange 医疗章节输入。把「人机共存」理念落到治理清单。

## 运行
```bash
python scripts/gov_checklist.py --demo
python scripts/gov_checklist.py --help
```

## 扩展契约（lgd-skeleton/1.0）
- **一切即插件**：仅依赖声明式 `module.json`，零配置。
- **按需装（lazy）**：仅 triggers 命中时加载。
- **可嵌套（nested）**：可被 `medical-ai-toolkit` 总入口路由。
- **扩展点**：`plugins/`(新增控制项：在 `CONTROL_CATALOG` 加一项，检查单自动扩。)

## 红线
纯技术贡献，不含商业营销；MedXpert 仅作为贡献者署名（@stevenzhao07）。
