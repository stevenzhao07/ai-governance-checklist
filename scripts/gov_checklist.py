#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gov_checklist.py — 医疗 AI 治理自检清单生成器
==============================================
从控制目录输出 Markdown 自检清单，覆盖：
  模型卡 / 数据卡 / 人类监督 / 公平性 / 安全 / 溯源 / 监测
零依赖（仅 Python 3.8+ 标准库）。把「人机共存」理念落到治理清单。
"""
from __future__ import annotations
import os
import sys
import argparse

CONTROL_CATALOG = {
    "model-card": [
        "已声明模型预期用途与禁用场景",
        "已给出性能指标准确区间与测试数据集",
        "已说明训练/验证/测试数据分布与潜在偏倚",
        "已标注模型局限性与失效模式",
    ],
    "data-card": [
        "已声明数据来源、授权与许可",
        "已说明采集人群与人口学覆盖",
        "已记录数据清洗/标注流程与质量度量",
        "已识别敏感属性与隐私保护措施",
    ],
    "human-oversight": [
        "已定义哪些决策需人类监督(human-in-the-loop)",
        "高风险动作已有显式确认/复核机制",
        "已定义人在回路失效时的回退路径",
        "已记录操作者与职责边界",
    ],
    "fairness": [
        "已识别受保护子组（性别/年龄/种族等）",
        "已计算子组性能差异并设可接受阈值",
        "已规划偏差缓解与再训练策略",
        "已文档化公平性评估结论",
    ],
    "security": [
        "已做威胁建模（SaMD/AIaMD 视角）",
        "已管控训练数据投毒与对抗样本风险",
        "已落实模型与数据访问鉴权",
        "已建立事件响应与披露流程",
    ],
    "provenance": [
        "已签发 AI 护照或等效身份档案",
        "已记录模型/数据版本与来源指纹",
        "已保留可审计的发布台账",
        "已声明第三方依赖与许可证",
    ],
    "monitoring": [
        "已定义上线后性能与漂移监测指标",
        "已建立 PMS/PMCF 反馈闭环",
        "已规划模型退役与变更控制(PCCP)",
        "已设置预警阈值与责任人",
    ],
}


def render(category: str | None) -> str:
    cats = {category: CONTROL_CATALOG[category]} if category else CONTROL_CATALOG
    out = ["# 医疗 AI 治理自检清单", "",
           "> 来源：ai-governance-checklist · 人机共存理念落地 · CC BY 4.0", ""]
    for cat, items in cats.items():
        out.append(f"## {cat}")
        for i, it in enumerate(items, 1):
            out.append(f"- [ ] {it}")
        out.append("")
    return "\n".join(out)


def _demo() -> int:
    print(render(None))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="医疗 AI 治理自检清单生成器")
    ap.add_argument("--demo", action="store_true", help="输出全部分类自检清单")
    ap.add_argument("--selftest", action="store_true", help="跑内置自测（断言 + 负对照 + xfail）")
    ap.add_argument("--all", action="store_true", help="输出全部分类")
    ap.add_argument("--category", help="仅输出指定分类: " + "/".join(CONTROL_CATALOG.keys()))
    ap.add_argument("--out", help="写入文件（否则打印到 stdout）")
    args = ap.parse_args()
    if getattr(args, "selftest", False):
        return _selftest()

    if args.demo:
        return _demo()

    if args.category and args.category not in CONTROL_CATALOG:
        print(f"[err] 未知分类。可选: {list(CONTROL_CATALOG)}")
        return 2
    cat = args.category if (args.category or not args.all) else None
    if not args.category and not args.all:
        args.all = True  # 默认全量

    md = render(args.category if args.category else (None if args.all else None))
    if args.out:
        # 自动创建父目录；失败给出友好错误而非裸 traceback（2026-10-12 压力测试修复）
        parent = os.path.dirname(os.path.abspath(args.out))
        try:
            os.makedirs(parent, exist_ok=True)
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(md)
        except OSError as e:
            print(f"[error] 无法写入 {args.out}: {e}", file=sys.stderr)
            return 2
        print(f"[ok] 已写 {args.out}")
    else:
        print(md)
    return 0


# ==================== 内置自测（--selftest） ====================
# 由 conformance 补丁于 2026-10-14 生成（生成器 v2）。
# 特性：端到端 CLI 调用 + 内容断言 + 负对照 + xfail（已知缺陷显式标注，不掩盖）。
_SELFTEST_CASES = [(['--demo'], 0, [], [], None), (['--all'], 0, [], [], None)]


def _selftest() -> int:
    import os as _os
    import subprocess as _sp
    _here = _os.path.dirname(_os.path.abspath(__file__))
    # 仓库根：脚本位于 <repo>/scripts/ 时取上一级；否则取脚本所在目录
    _root = _os.path.dirname(_here) if _os.path.basename(_here) == "scripts" else _here
    _script = _os.path.abspath(__file__)
    _fail, _xfail, _n = [], [], 0
    for _case in _SELFTEST_CASES:
        _args, _rc, _must, _mustnot = _case[0], _case[1], _case[2], _case[3]
        _reason = _case[4] if len(_case) > 4 else None
        _n += 1
        _p = _sp.run([sys.executable, _script] + _args, capture_output=True, cwd=_root)
        _out = _p.stdout.decode("utf-8", "replace")
        _bad = []
        if _p.returncode != _rc:
            _bad.append(f"rc={_p.returncode} 期望 {_rc}")
        for _m in _must:
            if _m not in _out:
                _bad.append(f"输出缺少 {_m!r}")
        for _m in _mustnot:
            if _m in _out:
                _bad.append(f"输出含禁止内容 {_m!r}")
        if _rc == 0 and not _out.strip():
            _bad.append("rc=0 但输出为空（假绿）")
        if _bad:
            if _reason:
                _xfail.append(f"xfail args={_args}：{'；'.join(_bad)} ← 已知缺陷：{_reason}")
            else:
                _fail.append(f"args={_args}：{'；'.join(_bad)}")
    # 通用负对照：未知参数必须非零
    _n += 1
    _p = _sp.run([sys.executable, _script, "--__nonexistent_flag__"], capture_output=True, cwd=_root)
    if _p.returncode == 0:
        _fail.append("负对照失败：未知参数竟返回 0")
    for _x in _xfail:
        print("[selftest][xfail] " + _x)
    if _fail:
        print(f"[selftest] FAILED {len(_fail)}/{_n}")
        for _f in _fail:
            print("  - " + _f)
        return 1
    print(f"[selftest] PASS {_n - len(_xfail)}/{_n}（含负对照；xfail {len(_xfail)} 项为已知缺陷）")
    return 0


if __name__ == "__main__":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
    raise SystemExit(main())
