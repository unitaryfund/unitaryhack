---
title: qBraid-QIR
emoji: 🐣 🛸
project_url: https://github.com/qBraid/qbraid-qir
metaDescription: qBraid-SDK extension providing support for QIR conversions.
date: 2024-05-15
summary: qBraid-SDK extension providing support for QIR conversions.
tags:
  - QIR
  - LLVM
  - Compiler
  - Cirq
  - OpenQASM
bounties:
  - issue_num: 67
    value: 150
  - issue_num: 70
    value: 150
  - issue_num: 78
    value: 75
  - issue_num: 80
    value: 50
  - issue_num: 90
    value: 75
---

Python package for generating [QIR](https://www.qir-alliance.org/) (Quantum Intermediate Representation) programs from high-level quantum programming languages. Currently supports conversions for Cirq and OpenQASM 3. This project aims to make QIR representations accessible via the [qBraid-SDK transpiler](https://github.com/qBraid/qBraid), and by doing so, open the door to language-specific conversions from any and all high-level quantum languages [supported](https://docs.qbraid.com/en/latest/sdk/overview.html#supported-frontends) by `qbraid`. See QIR Alliance: [why do we need it?](https://www.qir-alliance.org/qir-book/concepts/why-do-we-need.html). This project was conceived in collaboration with [QOSF](https://qosf.org/) (Quantum Open Source Foundation).

Quantum Intermediate Representation (QIR) was designed and developed with the same interoperability objectives as LLVM. In fact, QIR is in LLVM. How is QIR different from other quantum IRs? There are not really any at the same level of abstraction/mode. This new approach allows for Multiple Level Intermediate Representation (MLIR) compiler systems. Tools and components that lower the instruction with MLIR approach can be reused for different source languages and target machines. It was initially [introduced](https://arxiv.org/pdf/2101.11365.pdf) for in machine learning workflows to facilitate compilation for co-processing. MLIR spans the abstraction levels from after source code to machine code generation, creating a space for compiler extensibility and reusability with different high-level languages and low-level targets.
