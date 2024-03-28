---
title: OpenQASM 3 Parser
emoji: 🌐🦀
project_url: https://github.com/Qiskit/openqasm3_parser/
metaDescription: Parser and semantic analyzer for the OpenQASM 3.0 language, used by Qiskit
date: 2024-03-28
summary: Parser and semantic analyzer for the OpenQASM 3.0 language, used by Qiskit
tags:
  - qiskit
  - rust
  - OpenQASM
  - parser
bounties:
  - TBD
---

`openqasm3_parser` provides a compiler front end for OpenQASM 3 language (OQ3).

In this document, this parser is referred to as `openqasm3_parser`.

Differences with the [OpenQASM reference parser](https://github.com/openqasm/openqasm) are
- The parser in `openqasm3_parser` is much more performant. A crude test with large source files showed parse time reduced by a factor of 80.
- `openqasm3_parser` performs semantic analysis.

For support from the community, please join the [Qiskit Slack community](https://qisk.it/join-slack). The channel `#open-qasm` might be a good place for questions on the development. 
