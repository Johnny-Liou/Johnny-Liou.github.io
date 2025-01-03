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
    </li>
</ul>


<h2>Past Projects</h2>
<ul>
    <li>
        <strong>Optimizing Compute Core Assignment for Dynamic Batch Inference in AI Inference Accelerators. [Feb. 2024 - Sep. 2024]</strong>
        <br>
        <strong>[ACM-SAC 2025]</strong>
        <br>
        I addressed the inefficiencies of handling inference workloads with dynamic batch sizes—such as object detection downstream tasks—on multicore AI inference accelerators, which typically benefit from static inference for further optimization. We proposed dynamically partitioning the input batch data into smaller batches and creating multiple model instances to process each partition in parallel.
        <br>
        As modern multicore accelerators support flexible configuration, the challenge now lies in determining the optimal number of model instances, the appropriate batch size for each model, and the assignment of compute cores among the models to minimize inference time. To address this problem, we constructed an accurate, profiling-based cost model and devised a dynamic programming algorithm to determine the best configuration. Experimental results indicate that our method achieves an average 3.05x higher throughput in multi-person pose estimation benchmarks compared to the EdgeTPU inference strategy.
    </li>
    <li>
        <strong>Role of Weight Stationarity for CIM Architecture [Jun. 2023 - Sep. 2023]</strong>
        <br>
        <strong>[IEDM 2023]</strong>
        <br>
        I focused on the role of weight stationarity in Compute-In-Memory (CIM) systems for BERT-Base and BERT-Large transformer models. I analyzed systematic difference of two architectures: (1) a fully weight-stationary system using Non-Volatile Memory (NVM)-based tiles, which had fast latency but massive area usage, and (2) a partially weight-stationary system that, while lower raw area usage, suffered from higher latency due to the need for reloading weights into Volatile Memory-based tiles. Additionally, I explored alternative architectures for partially weight-stationary systems, identifying design choices that optimized area-compute efficiency (TOPS/sec/sq.mm) across various sequence lengths and input batch sizes.
    </li>
    <li>
        <strong>CIM-Aware Post-Training Quantization for Vision Transformer [Jul. 2022 - Jul. 2023]</strong>
        <br>
        Quantizing vision transformer models often leads to substantial accuracy loss due to severe inter-channel variation within the LayerNorm layer’s inputs. To tackle this challenge on Compute-In-Memory (CIM) systems—known for their high-throughput and energy-efficient Multiply-Accumulate operations—I proposed a CIM-aware group quantization method to effectively manage outlier data. Additionally, I made modifications to the peripheral circuitry to support this quantization approach with minimal overhead. Experimental results demonstrate that this method preserves model accuracy while reducing the LayerNorm layer’s inference energy by 25%.
    </li>
</ul>