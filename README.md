# Quantitative Risk Framework (MSc Thesis Blueprint)

A structural security framework designed to model, quantify, and propagate cascading cyber risks across complex enterprise networks. This repository contains the original classical models, adjacency matrices, and graph architectures developed during my **MSc in Data Science at Edinburgh University **. 

This research serves as the direct logical foundation for the next-generation **QCNN Quantum Bayesian Risk Evaluator** framework.

---

## 📊 Overview & Methodology

The core engine maps out enterprise attack surfaces by parsing infrastructure topologies into a **Directed Acyclic Graph (DAG)**. It utilizes structural dependency logic rules (leveraging MulVal/IDS threat outputs) to evaluate how an initial vulnerability exploit ripples conditionally through security boundaries (e.g., Firewalls, DMZs) to compromise critical backend assets.

### Key Classical Assets:
* **Network Topologies (`NewNet.xdsl`):** Graphical network models created in GeNIe/SMILE, specifying strict Conditional Probability Tables (CPTs) and asset dependency nodes.
* **Adjacency Matrices (`VERTICES.CSV` / `ARCS.CSV`):** Clean matrix data sheets cataloguing every infrastructure vertex and the directional edges binding them together.
* **Algorithmic Modeling (`attack_graph.py`):** The logical linkage system tracing multi-stage attack paths.

---
[ THIS REPOSITORY ]                 [ QUANTUM EVALUATION CORE ]
VERTICES & ARCS    ===========>    1. Qubit Wire Allocation
(Asset Graph Layout)               (Maps 32 Classical Nodes to Wires)
|                                      |
v                                      v
NewNet.xdsl      ===========>    2. QBN Feature Loader
(Dependency Arrows)                (Controlled RY Rotations Embed Math)
|
v
Classical MCMC    ===========>    3. QCNN Variational Aggregator
(Baseline Control)                 (Trainable Convolutional/Pooling Layers)

---
## 🧬 The Quantum Transition: Bridging Classical to Quantum

While this classical framework relies on static probabilities and sampling methods to estimate risk, its core architecture has been elevated into a live, **Hybrid Quantum Computing Pipeline**. 

The files in this repository map directly into the quantum space through three core phases:

### 1. Structure as a Quantum Blueprint
We treat the **`VERTICES.CSV`** and **`ARCS.CSV`** matrices as a permanent structural layout. Instead of rewriting network graphs from scratch, our quantum engine reads these files natively to dynamically spin up a **32-qubit register**. Your classical assets are cleanly mapped onto computational wires.

### 2. Causal Arrows as Controlled Gates
The conditional arrows inside **`NewNet.xdsl`** define our quantum gate configurations. For root nodes, live threat metrics (NIST NVD & FIRST EPSS) determine single-qubit \(R_Y\) rotations. For dependent paths, your classical CPT structures translate into multi-controlled \(CR_Y\) gates, causing risk states to propagate simultaneously via quantum interference.

### 3. Classical Monte Carlo as a Benchmark Control
In this repository, **Monte Carlo sampling** is used to approximate cascading path risks classically. In the expanded quantum framework, this classical engine is retained as the **Baseline Control**. We run both models side-by-side to directly plot execution speed, accuracy, and scaling curves, proving the computational advantage of the quantum pipeline.

---

## 🛠️ Original Legacy File Directory

* `NewNet.xdsl` — Primary GeNIe Bayesian network configuration layout.
* `NewNet_SecPolicy1.xdsl` to `8.xdsl` — Scripted variations testing specific security policy implementations.
* `VERTICES.CSV` — Complete catalogue of threat graph node identifiers.
* `ARCS.CSV` — Directed edge listings binding parents to child nodes.
* `attack_graph.py` — Legacy classical logic mapping utility.
