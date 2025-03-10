---
title: QuantumToolbox.jl
emoji:
project_url: https://github.com/qutip/QuantumToolbox.jl
metaDescription: Julia Package for Quantum Optics and Quantum Physics
date: 2024-04-01
summary: Julia Package for Quantum Optics and Quantum Physics
tags:
  - lindblad
  - optics
  - julia
bounties:
  - issue_num: 81
    value: 125
  - issue_num: 82
    value: 125
  - issue_num: 84
    value: 125
  - issue_num: 95
    value: 125
---

# QuantumToolbox

<div class="badges" markdown="1">

  <div class="badge" markdown="2">

[![Dev](/assets/img/docs-dev-blue.svg)](https://albertomercurio.github.io/QuantumToolbox.jl/dev)

  </div>

  <div class="badge" markdown="2">

[![Stable](/assets/img/docs-stable-blue.svg)](https://albertomercurio.github.io/QuantumToolbox.jl/stable)

  </div>

  <div class="badge" markdown="2">

[![Build-Status](/assets/img/build-status.svg)](https://github.com/albertomercurio/QuantumToolbox.jl/actions/workflows/CI.yml?query=branch%3Amain)

  </div>

  <div class="badge" markdown="2">

[![Coverage](/assets/img/coverage.svg)](https://codecov.io/gh/albertomercurio/QuantumToolbox.jl)

  </div>

  <div class="badge" markdown="2">

[![DOI](/assets/img/DOI.svg)](https://doi.org/10.5281/zenodo.10822817)

  </div>
</div>

## Introduction

[QuantumToolbox.jl](https://github.com/albertomercurio/QuantumToolbox.jl) is a cutting-edge Julia package designed for quantum physics simulations, closely emulating the popular Python [QuTiP](https://github.com/qutip/qutip) package. It uniquely combines the simplicity and power of Julia with advanced features like GPU acceleration and distributed computing, making simulation of quantum systems more accessible and efficient.

## Features

QuantumToolbox.jl is equipped with a robust set of features:

- **Quantum State and Operator Manipulation:** Easily handle quantum states and operators with a rich set of tools.

- **Dynamical Evolution:** Advanced solvers for time evolution of quantum systems.

- **Measurement and Statistics:** Comprehensive quantum measurement simulation and analysis.

- **GPU and Distributed Computing:** Leverage GPU and distributed resources for high-performance computing.

## Installation

```julia
using Pkg

Pkg.add("QuantumToolbox")
```
