---
title: Qibo
emoji: 🐪
project_url: "https://github.com/qiboteam/qibo"
metaDescription: An end-to-end open source platform for quantum simulation, self-hosted quantum hardware control, calibration and characterization.
date: 2025-03-31
summary: An end-to-end open source platform for quantum simulation, self-hosted quantum hardware control, calibration and characterization.
tags:
  - python
  - quantum simulation
  - hardware control
  - calibration
  - characterization
  - benchmarking
---

Qibo is designed with three target goals: a simple application programming interface (API) for quantum circuit design and adiabatic quantum computation, a high-performance simulation engine based on hardware acceleration tools, with particular emphasis on multithreading CPU, single GPU and multi-GPU setups, and ﬁnally a clean design pattern to include classical/quantum hybrid algorithms.

Recently,  we introduced Qibolab as a submodule of Qibo. This module includes primitives for managing the experimental setups required for quantum computing. With Qibolab, both low-level experiments and Qibo circuits can be executed on self-hosted quantum devices, which are increasingly becoming available for in-house use in research institutions.

Qibocal, which is based on both Qibo and Qibolab, was developed to ease the deployment of calibration protocols on superconducting devices.

Moreover, we have recently developed Qibotn, a Qibo subpackage that enables the execution of quantum circuits using tensor network-like computations, allowing to support of large-scale simulation of quantum circuits in Qibo. Qibotn interfaces Qibo with state-of-the-art quantum TN simulation libraries such as CuTensorNet (NVIDIA) and quimb.