---
title: 'ReplaySSM: Cache SSM Inputs, Not State'

authors:
  - me
  - H. Nover
  - A. Naik
  - A. Skliar
  - I. Shovkun
  - I. Shahaf
  - T. Dao

date: '2026-10-09T00:00:00Z'
publishDate: '2026-10-09T00:00:00Z'

publication_types: ['article']

publication: "arXiv preprint arXiv:2610.13778"
publication_short: "arXiv 2026"

abstract: "State-space models (SSMs) maintain a fixed-size recurrent state, but reading and writing it at every decoding step can bottleneck hybrid models. This eager state management causes large state I/O with low arithmetic intensity, leaves speculative decoding no cheap rollback, and feeds state quantization error into subsequent recurrent updates. We introduce ReplaySSM, which unrolls the recurrence to represent the state as a checkpoint and a buffer of recent SSM inputs. This separates output computation from checkpoint updates. By updating the checkpoint periodically, ReplaySSM avoids state writes on most steps and roughly halves the dominant state memory traffic. Keeping recent inputs also makes speculative rollback a buffer-pointer operation and enables output-only verification without materializing intermediate states. The same separation allows a low-precision checkpoint to serve output computation on most steps while a higher-precision checkpoint serves recurrent updates, so rounding error in the low-precision copy never enters later updates. We implement ReplaySSM in vLLM for Mamba-2 and Gated DeltaNet. At serving batch size 256, it accelerates standard decoding by 1.20–1.47× over a tuned vLLM baseline across four hybrid models, and delivers about 1.8× the throughput of vLLM's speculative decoding on the two 120B-class models. Separate state precisions also reduce output KL divergence and downstream accuracy losses compared with a shared low-precision checkpoint."

tags:
  - State-Space Models
  - Hybrid Models
  - LLM Inference
  - Speculative Decoding
  - ML Systems

featured: true

# Short notes rendered under the citation (see layouts/_partials/views/citation.html)
highlights:
  - '🚀 **Deployed in large-scale production models:** [**GLM-5.3-Flash**](https://z.ai/blog/glm-built-its-inference-infrastructure#:~:text=the%20LM%20Head%2C-,ReplaySSM,-%2C%20W8A8%20quantization%2C%20mixed), [**Kimi-K3**](https://arxiv.org/pdf/2607.24653#page=24)'
  - '🔧 Integrated into **vLLM** ([PR](https://github.com/vllm-project/vllm/pull/48018), [blog](https://vllm.ai/blog/2026-09-13-kimi-k3-performance-optimization#replayssm-reconstruct-the-kda-state-instead-of-storing-it)), **TensorRT-LLM** ([PR](https://github.com/NVIDIA/TensorRT-LLM/pull/14203), [PR](https://github.com/NVIDIA/TensorRT-LLM/pull/16464)), **FlashInfer** ([PR](https://github.com/flashinfer-ai/flashinfer/pull/3975), [PR](https://github.com/flashinfer-ai/flashinfer/pull/4081)), **SGLang** ([docs](https://lmsysorg.mintlify.app/cookbook/autoregressive/Qwen/Qwen3.8#replayssm))'
  - '📝 Featured on the [**NVIDIA Technical Blog**](https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/)'

links:
  - type: pdf
    label: Paper
    url: https://arxiv.org/pdf/2610.13778
  - type: code
    label: Code
    url: https://github.com/Johnny-Liou/ReplaySSM
  - type: site
    label: NVIDIA Blog
    icon: hero/newspaper
    url: https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/
  - type: site
    label: Dao AI Lab Blog
    icon: hero/newspaper
    url: https://dao-lab.ai/blog/2026/replayssm/

# Note: no `hugoblox.ids.arxiv` here on purpose; it would add a second "Preprint" button next to "Paper".

slides: ""
---
