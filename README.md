# Auto Proteomics

English | 中文

Auto Proteomics is a public OpenClaw skill for low-token routing and downstream analysis of processed DDA LFQ proteomics inputs.

Auto Proteomics 是一个公开的 OpenClaw skill，用于对 processed DDA LFQ 蛋白组学输入进行低 token 路由与 downstream 分析。

## What this release is

- one shipped runnable workflow: `dda-lfq-processed`
- one public input family: processed DDA LFQ protein-level tables
- one public comparison model: `group-a` vs `group-b`

## 当前版本是什么

- 一个已经随包提供并可运行的工作流：`dda-lfq-processed`
- 一类公开支持输入：processed DDA LFQ 蛋白层级定量表
- 一种公开比较模型：`group-a` vs `group-b`

## What it does

Given processed inputs such as MaxQuant-style `proteinGroups.txt`, this release provides a clear public path for:
- matrix generation
- QC outputs
- two-group differential protein analysis
- report and run manifest generation

给定类似 MaxQuant `proteinGroups.txt` 的 processed 输入，本版本提供一条清晰的公开路径，用于生成：
- matrix
- QC 输出
- 双组差异蛋白分析
- report 和 run manifest

## What it is not

This first public release is intentionally narrow. It does not promise:
- raw-spectrum identification pipelines
- DIA execution
- phosphoproteomics execution
- enrichment execution
- multi-omics execution
- generalized complex study-design handling

这个首个公开版本刻意保持边界收束，不承诺：
- 原始谱图鉴定流程
- DIA 执行
- 磷酸化蛋白组执行
- 富集分析执行
- multi-omics 执行
- 更一般化的复杂实验设计处理

## Public entrypoint

```bash
bash scripts/workflows/dda_lfq_processed.sh \
  --input-dir <run_dir> \
  --protein-groups <proteinGroups.txt> \
  --summary <summary.txt> \
  --parameters <parameters.txt> \
  --output-dir <output_dir> \
  --group-a <condition_a> \
  --group-b <condition_b>
```

## Repository structure

- `SKILL.md`: public entry and release boundary
- `references/WORKFLOW_INDEX.yaml`: routing and shipped-vs-scaffold boundary
- `references/RUNTIME_REQUIREMENTS.md`: runtime contract
- `references/DEMO_INPUT_GUIDE.md`: demo/onboarding input guidance
- `scripts/workflows/dda_lfq_processed.sh`: shipped execution path

## Release positioning

This repository is not presented as a full proteomics toolbox.
It is a clear, honest, directly runnable processed DDA LFQ downstream public skill.

这个仓库并不是“蛋白组学全家桶”。
它当前的对外定位是：一个架构清楚、对外诚实、能直接试跑的 processed DDA LFQ downstream public skill。
