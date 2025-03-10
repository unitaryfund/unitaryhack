---
title: AI-inspired Classification of Quantum Computers
id: qc-classifier
emoji: 🧙‍♂️
project_url: https://github.com/dorahacksglobal/qc-classifier
metaDescription: Is it possible to distinguish the given random numbers are produced from a specific quantum computer? More generally, this problem is related to the topic of cross-platform comparison of quantum circuits.
date: 2024-04-16
summary: Is it possible to distinguish the given random numbers are produced from a specific quantum computer? More generally, this problem is related to the topic of cross-platform comparison of quantum circuits.
tags:
  - DI-QRNG
  - Classification
  - Cloud QC
bounties:
  - issue_num: 1
    value: 150
  - issue_num: 3
    value: 150
  - issue_num: 2
    value: 200
---

Quantum computers promise diverse applications with fault-tolerant architectures. Near-term quantum computers are comprised of different physical entities, such as superconducting qubits, propagating photons, trapped ions and tweezer-based neutral atoms.

Randomness lies in the cornerstone of quantum mechanics, especially in the dispute of reality and non-locality [1]. After decades of experimental progress [2], loophole-free Bell inequality was demonstrated by several groups using photons [3, 4] and superconducting qubits [5]. As a result, device-independent certified quantum random number generator [6] and randomness expansion [7, 8] are cutting-edge and realistic applications. Besides, one of the potential applications of NISQ quantum advantages (e.g. random circuits sampling) is also certified randomness [9, 10].

Current cloud-based quantum computers service is ready for producing quantum random numbers for cryptography. However, due to the notorious decoherence processes, the raw entanglement between isolated qubits is deteriorated without any digital error-mitigation technique (like readout correction). Thus, we are curious about the randomness degradation. More specifically, is it possible to distinguish the given random numbers are produced from a specific quantum computer?

Take the output from a quantum random number generator as training data, the data is produced by different IBMQ simulators (including noise). Find a way to create a model that classifies new random number output, and identifies which machine the random number is produced from. The quantum random number generator functions as described in https://github.com/dorahacksglobal/quantum-randomness-generator. Run experiments by yourself, and compare different models. Is this classification task possible? What are the possible ways to improve the model so that it's useful?

More generally, this problem is related to the topic of cross-platform comparison of quantum circuits [11, 12].

A series of benchmark experiments was performed and [recorded here](https://github.com/dorahacksglobal/quantum-randomness-generator/blob/QC-Prediction-Model/classification/RandomNumber_Classification.ipynb).

Later during the Yale Quantum Hackathon 2024, a challenge was posted by [DoraHacks team](https://dorahacks.io/hackathon/yquantum2024/dorahacks-challenge-track). The challenge was attempted by 7 teams. One of the teams has made material progress to [improve prediction accuracy from the benchmark results](https://dorahacks.io/buidl/11292).

The DoraHacks team is currently working on [further improvements](https://github.com/dorahacksglobal/quantum-randomness-generator/tree/QC-Prediction-Model/classification).

For this challenge, please build on top of the most recent progress and improve the prediction accuracy. The bounty winner will go to the team / individual that produces the best results. We haven't explored this on general quantum circuits, progress on general circuits can claim separate / additional bounty prizes.

## Resources:

[1] Einstein, Albert, Boris Podolsky, and Nathan Rosen. "Can quantum-mechanical description of physical reality be considered complete?." Physical review 47.10 (1935): 777.

[2] Hensen, Bas, et al. "Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres." Nature 526.7575 (2015): 682-686.

[3] Giustina, Marissa, et al. "Significant-loophole-free test of Bell’s theorem with entangled photons." Physical review letters 115.25 (2015): 250401.

[4] Shalm, Lynden K., et al. "Strong loophole-free test of local realism." Physical review letters 115.25 (2015): 250402.

[5] Storz, Simon, et al. "Loophole-free Bell inequality violation with superconducting circuits." Nature 617.7960 (2023): 265-270.

[6] Abellán, Carlos, et al. "Generation of fresh and pure random numbers for loophole-free Bell tests." Physical review letters 115.25 (2015): 250403.

[7] Liu, Wen-Zhao, et al. "Device-independent randomness expansion against quantum side information." Nature Physics 17.4 (2021): 448-451.

[8] Shalm, Lynden K., et al. "Device-independent randomness expansion with entangled photons." Nature Physics 17.4 (2021): 452-456.

[9] Aaronson, Scott, and Shih-Han Hung. "Certified randomness from quantum supremacy." Proceedings of the 55th Annual ACM Symposium on Theory of Computing. 2023.

[10] Morvan, Alexis, et al. "Phase transition in random circuit sampling." arXiv preprint arXiv:2304.11119 (2023).

[11] Zhu, Daiwei, et al. "Cross-platform comparison of arbitrary quantum states." Nature communications 13.1 (2022): 6620.

[12] Elben, Andreas, et al. "Cross-platform verification of intermediate scale quantum devices." Physical review letters 124.1 (2020): 010504.
