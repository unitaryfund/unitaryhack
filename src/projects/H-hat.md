---
title: H-hat quantum programming language
emoji: 🎩👒
project_url: https://github.com/hhat-lang/hhat_lang
metaDescription: H-hat is a quantum programming language that aims to bring quantum resources to software developers with no prior knowledge on quantum computing.
date: 2025-03-25
summary: H-hat is a quantum programming language that aims to bring quantum resources to software developers with no prior knowledge on quantum computing.
tags:
  - programming language
  - compiler
---

**What H-hat is**

- A quantum programming language family and the ecosystem to build it
- An abstraction layer above QASM-like languages
- A language to
    - Use higher-level abstraction to harness quantum resources, such as superposition, entanglement, etc.
    - Need no specialized knowledge on quantum mechanics or quantum information theory
    - Close the gap between developers/programmers/computer scientists and quantum physicists
    - Use quantum data and quantum data structures to reason about quantum information processing
    - Solve problems using quantum logic, but not raw quantum mechanics approach

**What H-hat is not**

- A replacement for quantum logic-level quantum computation (circuit-like quantum computing, for instance), such as QASM-like languages
- A full stack programming language with direct access to the hardware
- A simulator

Language features

- Code reasoning closer to classical programming languages
- Quantum data types, variables, functions just as its classical counterpart
- Additionally, there is quantum primitives to define some general platform-dependent instruction set
- Classical and quantum parts have similar syntaxes and components
- Quantum variables:
    - hold quantum and classical instructions
    - execute its content and perform measurement once a cast function is called upon it
    - re-execute the same data content every time it is cast
- Platform- and quantum logic language- independent
- Can hold many syntaxes/dialects implementations to work in harmony with each other
