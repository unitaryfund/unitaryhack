---
title: PennyLane Plugin for Amazon Braket
id: amazon-braket-pennylane-plugin-python
emoji: ⚛️🪙
project_url: https://github.com/amazon-braket/amazon-braket-pennylane-plugin-python
metaDescription: Plugin allowing PennyLane to use Amazon Braket quantum hardware and simulators
date: 2024-05-15
summary: Plugin allowing PennyLane to use Amazon Braket quantum hardware and simulators
tags:
  - Amazon Braket
  - Python
  - PennyLane
bounties:
  - issue_num: 179
    value: 90
  - issue_num: 195
    value: 70
  - issue_num: 255
    value: 90
---

The Amazon Braket PennyLane plugin offers four Amazon Braket quantum devices to work with PennyLane:

- `braket.aws.qubit` for running with the Amazon Braket service's quantum devices, both QPUs and simulators
- `braket.local.qubit` for running the Amazon Braket SDK's local simulator where you can optionally specify the backend ("default", "braket_sv", "braket_dm", etc.)
- `braket.aws.ahs` for running with the Amazon Braket service's analog Hamiltonian simulation QPUs
- `braket.local.ahs` for running analog Hamiltonian simulation on Amazon Braket SDK's local simulator

[PennyLane](https://pennylane.readthedocs.io/) is a machine learning library for optimization and automatic differentiation of hybrid quantum-classical computations.

[Amazon Braket](https://aws.amazon.com/braket/) is a fully managed quantum computing service designed to help speed up scientific research and software development for quantum computing.
