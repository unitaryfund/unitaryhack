---
title: Perceval
emoji:
project_url: https://github.com/Quandela/Perceval
metaDescription: A linear optics simulation framework for quantum computing
date: 2024-05-27
summary: A linear optics simulation framework for quantum computing
tags:
  - Quantum
  - Photonics
  - Python
bounties:
  - issue_num: 399
    value: 200
  - issue_num: 400
    value: 200
  - issue_num: 207
    value: 100
---

Through a simple object-oriented python API, Perceval provides tools for building a circuit with linear optics components, defining single-photon sources and their error model, manipulating Fock states, running simulations, reproducing published experimental papers results, and experimenting a new generation of quantum algorithms.

It is interfaced with the available QPUs on the [Quandela cloud](https://cloud.quandela.com/webide/), so it is possible to run computations on an actual photonic computer.

Perceval aims to be a companion tool for developing discrete-variable photonics circuits

- while simulating their design, modeling their ideal and real-life behaviour;
- and proposing a normalized interface to control photonic quantum computers
- while using powerful simulation backends to get state-of-the-art simulation;
- and also allowing direct access to the QPUs of Quandela.

Perceval has been developed as a complete toolkit for physicists and quantum computational students, researchers and practitioners.

**Key Features**
- Powerful Circuit designer making use of predefined components
- Simple python API and powerful simulation backends optimized in C++
- Utilities to manipulate State Vector, Unitary Matrices, and circuit Parameters
- Transversal tools for visualization compatible with notebooks or local development environments
- Modular architecture welcoming contributions from the community
