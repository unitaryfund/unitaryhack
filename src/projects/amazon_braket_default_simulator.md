---
title: Amazon Braket Default Simulator
id: amazon-braket-default-simulator-python
emoji: ⚛️📊
project_url: https://github.com/amazon-braket/amazon-braket-default-simulator-python
metaDescription: Provides an implementation of quantum simulators that can run locally, meant to be compatible with the Amazon Braket SDK
date: 2024-05-15
summary: Provides an implementation of quantum simulators that can run locally, meant to be compatible with the Amazon Braket SDK
tags:
  - Amazon Braket
  - Python
  - quantum circuits
  - OpenQASM
  - simulators
bounties:
  - issue_num: 252
    value: 100
  - issue_num: 253
    value: 70
  - issue_num: 240
    value: 70
---

The Amazon Braket Default Simulator is a Python open source library that provides an implementation of a quantum simulator that you can run locally. You can use the simulator to test quantum tasks that you construct for the [Amazon Braket SDK](https://github.com/amazon-braket/amazon-braket-sdk-python) before you submit them to the Amazon Braket service for execution.

The library includes an implementation of quantum simulators that can run circuits on your local, classical hardware. For example, the braket_sv local simulator is well suited for rapid prototyping on small circuits up to 25 qubits, depending on the hardware specifications of your Braket notebook instance or your local environment. An example of how to execute the quantum task locally is included in the repository.

For a list of available simulators and their features, consult the [Amazon Braket Developer Guide](https://docs.aws.amazon.com/braket/latest/developerguide/braket-devices.html).
