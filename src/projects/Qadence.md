---
title: Qadence
emoji:
project_url: https://github.com/pasqal-io/qadence
metaDescription: Qadence is a Python package that provides a simple interface to build digital-analog quantum programs with tunable qubit interaction defined on arbitrary register topologies realizable on neutral atom devices.
date: 2024-04-02
summary: Qadence is a Python package that provides a simple interface to build digital-analog quantum programs with tunable qubit interaction defined on arbitrary register topologies realizable on neutral atom devices.
tags:
  - Digital Analog
  - Differentiability
bounties:
  - issue_num: 370
    value: 100
  - issue_num: 368
    value: 100
  - issue_num: 268
    value: 50
  - issue_num: 214
    value: 150
  - issue_num: 40
    value: 100
---

## Feature highlights

- A block-based system for composing _**complex digital-analog programs**_ in a flexible and scalable manner, inspired by the Julia quantum SDK [Yao.jl](https://github.com/QuantumBFS/Yao.jl) and functional programming concepts.
- A simple interface to work with _**interacting neutral-atom qubit systems**_ using arbitrary registers topologies.
- An intuitive expression-based system developed on top of the symbolic library [Sympy](https://www.sympy.org/en/index.html) to construct _**parametric quantum programs**_ easily.
- High-order generalized parameter shift rules for _**differentiating parametrized quantum operations**_.
- Out-of-the-box _**automatic differentiability**_ of quantum programs with [PyTorch](https://pytorch.org/) integration.
- _**Efficient execution**_ on a variety of different purpose backends: from state vector simulators to tensor network emulators and real devices.
