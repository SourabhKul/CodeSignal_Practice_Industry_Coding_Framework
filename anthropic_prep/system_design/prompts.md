# System Design Practice Prompts

Use these for 35-45 minute whiteboard drills.

## High-Concurrency Inference API

Design an LLM inference API.

Must discuss:

- Request lifecycle and streaming responses.
- Dynamic batching of variable-length requests.
- KV cache memory pressure and eviction.
- GPU scheduling and priority queues.
- Rate limits, retries, cancellation, and backpressure.
- Observability: queue time, prefill time, decode throughput, GPU memory.

## Prompt Playground / Chat Service

Design a Claude-like chat or prompt playground.

Must discuss:

- Conversation persistence and autosave.
- Streaming token delivery.
- Client reconnect/resume.
- Branching, edits, and versioned prompts.
- Tool calls and long-running jobs.
- Abuse/rate limiting and audit logs.

## Large Model File Distribution

Design distribution for 500GB model files across many machines.

Must discuss:

- Chunking, manifests, checksums, and resumable downloads.
- Regional caches and peer-to-peer options.
- Rollout safety and version pinning.
- Bandwidth shaping and blast-radius limits.
- Verification before activation.

