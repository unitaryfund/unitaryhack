---
title: BraketAHS.jl
emoji: ⚛️🌊
project_url: https://github.com/amazon-braket/BraketAHS.jl
metaDescription: Tensor network simulator for analog Hamiltonian simulation
date: 2024-05-15
summary: Tensor network simulator for analog Hamiltonian simulation
tags:
  - Amazon Braket
  - Python
  - Analog Hamiltonian simulation
bounties:
  - issue_num: 13
    value: 60
  - issue_num: 14
    value: 110
  - issue_num: 15
    value: 70
---

This package implements a tensor network based algorithm for simulating Rydberg atom dynamics. It allows to simulate Analog Hamiltonian Simulation programs for problem sizes of hundreds of atoms, which is unaccessible by statevector simulation methods. Matrix Product States (MPS) are used to represent the many-body quantum state.

The core of the tensor network simulation is enabled by [iTensor.jl](https://github.com/ITensor/ITensors.jl). The input Analog Hamiltonian Simulation (AHS) program can be constructed using [Braket.jl](https://github.com/amazon-braket/Braket.jl) interface.
