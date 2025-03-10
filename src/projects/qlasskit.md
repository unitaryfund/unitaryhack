---
title: qlasskit
emoji: ⚙️
project_url: https://github.com/dakk/qlasskit
metaDescription: A python-to-quantum compiler
date: 2024-03-28
summary: A python-to-quantum compiler
tags:
  - compilation
bounties:
  - issue_num: 26
    value: 100
  - issue_num: 28
    value: 100
  - issue_num: 23
    value: 50
  - issue_num: 27
    value: 100
  - issue_num: 32
    value: 75
---

Qlasskit is a Python library that empowers quantum developers to write classical algorithms in pure Python and translate them into quantum circuits seamlessly. This is particularly valuable in scenarios where classical computation must be integrated into a quantum algorithm or to define an oracle. To convert Python code into a quantum circuit, Qlasskit employs a multipass compiler. Starting from the original Python AST, the code is transformed into boolean expressions. Finally, the simplified expressions are compiled into a quantum circuit. Qlasskit supports exporting to major quantum frameworks (Qiskit, Pennylane, Cirq, Qutip, etc) and also enables exporting to Binary Quadratic Models (BQM), including Ising and QUBO, ready to be utilized in quantum annealers, Ising machines and simulated samplers.
