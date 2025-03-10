---
title: rustworkx
emoji: ⚙️
project_url: https://github.com/Qiskit/rustworkx
metaDescription: A high performance Python graph library implemented in Rust, used by Qiskit
date: 2024-03-28
summary: A high performance Python graph library implemented in Rust, used by Qiskit
tags:
  - qiskit
  - rust
  - graph theory
bounties:
  - issue_num: 774
    value: 75
  - issue_num: 750
    value: 75
  - issue_num: 804
    value: 100
  - issue_num: 803
    value: 200
---

A high-performance, general-purpose graph library for Python, written in Rust. You can see the full rendered docs at: https://www.rustworkx.org/

Rustworkx was originally called retworkx and was created initially to be a replacement for [Qiskit's](https://www.ibm.com/quantum/qiskit) previous (and current) NetworkX usage (hence the original name). The project was originally started to build a faster directed graph to use as the underlying data structure for the DAG at the center of [Qiskit's](https://www.ibm.com/quantum/qiskit) transpiler. However, since it's initial introduction the project has grown substantially and now covers all applications that need to work with graphs which includes Qiskit.

There are two locations available to talk to other rustworkx users and developers. The first is a public Slack channel in the Qiskit workspace, `#rustworkx`. You can join the Qiskit Slack workspace [here](https://qisk.it/join-slack). Additionally, there is an IRC channel `#rustworkx` on the [OFTC IRC network](https://www.oftc.net/).
