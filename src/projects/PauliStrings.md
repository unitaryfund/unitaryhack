---
title: PauliStrings.jl
emoji: 🧶
project_url: "https://github.com/nicolasloizeau/PauliStrings.jl"
metaDescription: Quantum many body simulations in the Pauli strings representation
date: 2025-04-04
summary: Quantum many body simulations in the Pauli strings representation
tags:
  - julia
  - quantum circuits
  - quantum simulation
  - pauli propagation
  - pauli strings
---

[PauliStrings.jl](https://paulistrings.org/) is a Julia package for high performance simulation of quantum many-body systems in the Pauli string basis. It is particularly adapted for running the  Lanczos algorithm (recursion method), time evolving noisy systems and simulating spin systems on arbitrary graphs.
The performance arises from two key features:
- The Pauli string algebra is encoded in low-level logic operations on integers, making it very efficient to store and multiply strings together.
- Operators can be systematically truncated to some precision by discarding strings with negligibly small weight. This allows one to keep the number of strings manageable at the cost of introducing some incurred error.