---
title: 'Optimizing Compute Core Assignment for Dynamic Batch Inference in AI Inference Accelerator'

authors:
  - me
  - D.-Y. Hong

date: '2025-03-01T00:00:00Z'
publishDate: '2025-03-01T00:00:00Z'

publication_types: ['paper-conference']

publication: "Proceedings of the 40th ACM/SIGAPP Symposium on Applied Computing"
publication_short: "ACM SAC '25"

abstract: "Modern AI inference accelerators offer high-performance and power-efficient computations for machine learning models. Most accelerators employ static inference to enhance performance, which requires models to be compiled with predetermined input batch sizes and intermediate tensor shapes. However, static inference can lead to program failures or inefficient execution when processing batched data of varying sizes, a scenario known as dynamic batch inference. This work addresses this challenge by focusing on the emerging multicore AI inference accelerators that offer flexible compute core assignment. We propose to dynamically partition the input batch data into smaller batches, and create multiple model instances to process each partition in parallel. The challenge lies in how to determine the optimal number of model instances, the proper batch size for each handling model, and the assignment of compute cores among the models, to minimize the inference time. To solve the problem, we construct an accurate profiling-based cost model and devise a dynamic programming algorithm to determine the best configuration. Experimental results indicate that our method achieves 3.05× higher throughput on average in multi-person pose estimation benchmarks, compared to the EdgeTPU-like inference strategy."

tags:
  - AI Inference
  - Dynamic Batch
  - ML Systems

featured: true

hugoblox:
  ids:
    doi: 10.1145/3672608.3707809

links: []
slides: ""
---
