---
title: qBraid-SDK
id: qbraid
emoji: 🏃‍♂️⏱️
project_url: https://github.com/qBraid/qBraid
metaDescription: Platform-agnostic quantum runtime framework designed for both quantum software and hardware providers.
date: 2024-05-08
summary: Platform-agnostic quantum runtime framework designed for both quantum software and hardware providers.
tags:
  - Python
  - Openqasm
  - Transpiler
  - Provider
  - Runtime
bounties:
  - issue_num: 626
    value: 150
  - issue_num: 618
    value: 75
  - issue_num: 619
    value: 125
  - issue_num: 624
    value: 75
  - issue_num: 625
    value: 75
---

The [qBraid-SDK](https://github.com/qBraid/qBraid) is a platform-agnostic quantum runtime framework designed for both quantum software and hardware providers.

This Python-based tool streamlines the full lifecycle management of quantum jobs&mdash;from defining program specifications to job submission, and through to the post-processing and visualization of results. Distinguishing itself through a streamlined and highly-configurable approach to cross-platform integration, the qBraid-SDK _does not assume a fixed target software framework_. Instead, it allows providers to dynamically register any desired run input program type as the target, depending on their specific needs. These program types are interconnected via a graph-based transpiler, where each program type is represented as a node and supported conversions as edges. The breadth, depth, and connectivity of this `ConversionGraph` can be customized by the provider.

The framework also facilitates the insertion of additional program validations, circuit transformations, and transpiler/compiler steps into its modular pipeline through a comprehensive `RuntimeProfile`. This profile encapsulates both device properties (such as number of qubits, maximum shots, native gate set) and the software requirements (`ProgramSpec`) needed to submit a job, vastly reducing the overhead and redundancy typically associated with cross-platform integrations in quantum computing.
