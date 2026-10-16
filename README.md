# ai-governance-checklist

> **Contributed by [@stevenzhao07](https://github.com/stevenzhao07) · Affiliation: MedXpert (medical-device RA & regulatory consultancy) · Pure technical input, no commercial promotion.**

医疗 AI 治理的聚合开源仓：模型卡 / 数据卡模板 + 人类监督（human-in-the-loop）检查单 + 公平性测试骨架 + OWASP AI Exchange 医疗章节输入。把「人机共存」理念落到治理清单。

这是 MedXpert 把"医疗 AI 信任"方法论工程化落地的可插拔模块之一——把抽象的合规要求变成一条可重复运行的命令或参考实现。方法论四要素（白话版）：**治理守护者 XCGS** ＝ 为 AI 留下可核验的治理证据；**立法者 A³ Laws** ＝ 给自主系统划权限 / 监督 / 追责三条硬边界；**护照官 AI 护照** ＝ 为模型签发可追溯的身份凭证；**人机共存** ＝ 明确人类与 AI 的分工与兜底。

---

## 可插拔模块契约（lgd-skeleton/1.0）

本仓库是一个 **`lgd-skeleton/1.0` 可插拔模块**：

- **一切即插件**：仅依赖声明式 `module.json`，零配置；
- **按需装（lazy）**：仅 triggers 命中时加载；
- **可嵌套（nested）**：可被 `medical-ai-toolkit` 总入口路由发现；
- **扩展点**：`plugins/`(新增控制项：在 `CONTROL_CATALOG` 加一项，检查单自动扩。)。

机器可发现入口：`AGENTS.md` · `CLAUDE.md` · `llms.txt`。

## 特性

- 治理检查单生成器：`gov_checklist.py` 从控制目录输出 Markdown 自检清单（模型卡/数据卡/人类监督/公平性/安全/溯源/监测）
- 模板：`templates/model_card.md` + `templates/data_card.md` 可直接复制填
- 人类监督检查单：高风险决策须人在回路的判定项
- 零依赖 + CLI：按类别过滤输出

**上游投稿目标**：OWASP AI Exchange / aiverify-foundation

## 内容说明

本仓混合许可：自创模板 CC BY 4.0；投向上游 OWASP AI Exchange（医疗章节）、aiverify-foundation（骨科公平性插件）。标准轨道以个人专家 Xinghua Zhao 名义参与社区贡献。

## 免责声明

本工具仅提供结构化模板与计算能力，**不构成法规建议、合规结论或专业意见**。医疗 AI / 医疗器械相关的落地决策，须由合资格人员依据目标辖区（NMPA / FDA / EU MDR / PMDA）最新法规文本作出；条款与限值以官方发布文本为准。使用本工具产生的一切后果由使用者自行承担。

## 使用

```bash
python scripts/gov_checklist.py --all
python scripts/gov_checklist.py --category human-oversight
```

## 快速开始（30 秒）

```bash
git clone https://github.com/stevenzhao07/ai-governance-checklist.git && cd ai-governance-checklist
python scripts/gov_checklist.py --demo
```

> 想参与或遇到问题？[提 Issue](https://github.com/stevenzhao07/ai-governance-checklist/issues) · 完整《AI 参与指南》见 [medical-ai-toolkit](https://github.com/stevenzhao07/medical-ai-toolkit)。

## 路由（总入口）

本模块由 **[medical-ai-toolkit](https://github.com/stevenzhao07/medical-ai-toolkit)** 作为 `lgd-skeleton/1.0` 总入口自动路由发现。

## 关联模块

- [ai-a3-laws](https://github.com/stevenzhao07/ai-a3-laws)
- [ai-model-passport](https://github.com/stevenzhao07/ai-model-passport)
- [ml-validation-toolkit](https://github.com/stevenzhao07/ml-validation-toolkit)

## 许可

CC-BY-4.0 — 见 [LICENSE](./LICENSE)。

## 关联（方法论来源）

- 理念溯源：个人专家关于医疗 AI 信任与治理的公开方法论（个人观点，不构成标准）
- 同账号系列：见 `medical-ai-toolkit` 导航
