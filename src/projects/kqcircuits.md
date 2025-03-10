---
title: KQCircuits
emoji: 🦑
project_url: https://github.com/iqm-finland/KQCircuits
metaDescription: KLayout Python library for integrated quantum circuit design.
date: 2024-03-27
summary: KLayout Python library for integrated quantum circuit design.
tags:
  - python
  - klayout
  - eda
  - lithography
bounties:
  - issue_num: 45
    value: 150
  - issue_num: 52
    value: 75
  - issue_num: 91
    value: 75
  - issue_num: 89
    value: 75
  - issue_num: 90
    value: 75
  - issue_num: 92
    value: 50
---

KQCircuits generates multi-layer 2-dimensional-geometry representing common structures in quantum processing units (QPU). It includes definitions of parametrized geometrical objects or “elements”, framework to easily define your own elements, framework to get geometry from the elements by setting values to parameters and a framework to assemble a full QPU design by combining many of the elements in different geometrical relations. Among other templates, are also structures to combine QPU designs to create optical mask layout and EBL patterns for fabrication of quantum circuits and export a set of files for a mask as needed for QPU fabrication. KQCircuits also provides a way to export designed geometry to be simulated by third-party simulators like Ansys and Elmer.
