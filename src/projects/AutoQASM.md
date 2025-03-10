---
title: AutoQASM
emoji: ⚛️🐍
project_url: https://github.com/amazon-braket/autoqasm
metaDescription: An experimental, imperative programming interface for developing quantum programs in native Python
date: 2024-05-15
summary: An experimental, imperative programming interface for developing quantum programs in native Python
tags:
  - Amazon Braket
  - Python
  - Programming interface
  - Mid-circuit measurement
  - OpenQASM
bounties:
  - issue_num: 9
    value: 50
  - issue_num: 10
    value: 50
  - issue_num: 11
    value: 50
  - issue_num: 12
    value: 60
  - issue_num: 13
    value: 40
---

AutoQASM provides a Pythonic developer experience for writing quantum programs. The name AutoQASM is derived from the name of the [AutoGraph module of TensorFlow](https://www.tensorflow.org/api_docs/python/tf/autograph). AutoQASM uses AutoGraph to construct quantum assembly (QASM) programs rather than TensorFlow graphs.

AutoQASM provides a natural interface for expressing quantum programs with mid-circuit measurements and classical control flow using native Python language features. It allows the construction of modular programs consisting of common programming constructs such as loops and subroutines. This enables a more imperative programming style than constructing programs via a series of function calls on a circuit object.

Although it is still a work in progress, the intent is that AutoQASM will support any quantum programming paradigm which falls into the [OpenQASM 3.0](https://openqasm.com/) language scope. AutoQASM supports serializing quantum programs to OpenQASM, which allows the programs to interoperate with any library or service that supports OpenQASM programs, such as Amazon Braket.
