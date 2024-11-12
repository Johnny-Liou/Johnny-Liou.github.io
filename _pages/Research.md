---
layout: page
permalink: /Research/
title: Research
description: 
nav: true
nav_order: 2
---

<h2>Current Project</h2>
<ul>
    <li>
        <strong>Flexible Hardware Accelerator for N:M Sparse Model</strong>
        <br>
        N:M structured pruning, where N elements are retained out of every M consecutive weight parameters, has shown performance comparable to unstructured pruning. Recent studies also indicate that layer-wise N:M structured pruning, which applies different N:M sparsity ratios to different layers, can further enhance accuracy. However, existing hardware, such as Nvidia's Sparse Tensor Core, only supports a fixed 2:4 pruning, which falls short of meeting the diverse sparsity requirements of modern AI workloads.
        <br>
        In this project, I developed a flexible, systolic array-based hardware accelerator capable of supporting arbitrary N:M sparsity ratios for both activations and weights. This design enables a single accelerator to dynamically support dense-dense, sparse-dense, and sparse-sparse matrix multiplication with minimal overhead. Additionally, leveraging the flexibility of this hardware, I introduced an intra-matrix block-wise N:M sparsity scheme, allowing different sparsity ratios to be applied to distinct blocks within a matrix based on weight distribution patterns. Preliminary results show that this approach enhances accuracy on BERT models across several GLUE benchmarks.
</ul>


<h2>Past Projects</h2>
    <ul>
        <li>
            <strong>Role of Weight Stationarity for CIM Architecture</strong>
            <p style="text-align: justify;">
            In this work, I focused on the role of weight stationarity in Compute-In-Memory (CIM) systems for BERT-Base and BERT-Large transformer models. I analyzed two architectures: (1) a fully weight-stationary system using Non-Volatile Memory (NVM)-based tiles, which had fast latency but massive area usage, and (2) a partially weight-stationary system that, while lower raw area usage, suffered from higher latency due to the need for reloading weights into Volatile Memory-based tiles. Additionally, I explored alternative architectures for partially weight-stationary systems, identifying design choices that optimized area-compute efficiency (TOPS/sec/sq.mm) across various sequence lengths and input batch sizes.
            </p>
        </li>
        <li>
            <strong>Role of Weight Stationarity for CIM Architecture</strong>
            <p style="text-align: justify;">
            In this work, I focused on the role of weight stationarity in Compute-In-Memory (CIM) systems for BERT-Base and BERT-Large transformer models. I analyzed two architectures: (1) a fully weight-stationary system using Non-Volatile Memory (NVM)-based tiles, which had fast latency but massive area usage, and (2) a partially weight-stationary system that, while lower raw area usage, suffered from higher latency due to the need for reloading weights into Volatile Memory-based tiles. Additionally, I explored alternative architectures for partially weight-stationary systems, identifying design choices that optimized area-compute efficiency (TOPS/sec/sq.mm) across various sequence lengths and input batch sizes.
            </p>
        </li>
        <li>
            <strong>Role of Weight Stationarity for CIM Architecture</strong>
            <p style="text-align: justify;">
            In this work, I focused on the role of weight stationarity in Compute-In-Memory (CIM) systems for BERT-Base and BERT-Large transformer models. I analyzed two architectures: (1) a fully weight-stationary system using Non-Volatile Memory (NVM)-based tiles, which had fast latency but massive area usage, and (2) a partially weight-stationary system that, while lower raw area usage, suffered from higher latency due to the need for reloading weights into Volatile Memory-based tiles. Additionally, I explored alternative architectures for partially weight-stationary systems, identifying design choices that optimized area-compute efficiency (TOPS/sec/sq.mm) across various sequence lengths and input batch sizes.
            </p>
        </li>
    </ul>