# Choosing a model

This cookbook doesn't hard-code any specific model. Every example reads the Groq
model ID it should use from an environment variable (or from a placeholder you can
edit at the top of the file/notebook), so you can plug in any model hosted on Groq.
See https://console.groq.com/docs/models for the current list.

| Variable | Used for |
|---|---|
| `GROQ_MODEL` | Chat / text generation (most examples) |
| `GROQ_SPEECH_MODEL` | Speech-to-text (audio chunking, subtitler, podcast RAG, Gradio voice app) |
| `GROQ_VISION_MODEL` | Image understanding (image processing, batch image analysis, image moderation) |
| `GROQ_GUARD_MODEL` | Content-safety / guard model (guardrails examples) |
| `GROQ_JUDGE_MODEL` | Second model for evaluation / judging (RAG benchmarking, agent evals) |
| `GROQ_MODEL_A` … `GROQ_MODEL_D` | Different models for the mixture-of-agents examples |
| `GROQ_LAYER_MODEL_1` … `_3` | Layer agents in the LangChain mixture-of-agents notebook |
| `GROQ_MODELS` | Comma-separated model IDs for the Streamlit apps' dropdowns |
| `LOCAL_MODEL` | Local Ollama model for the Minions example |

Example:

```bash
export GROQ_API_KEY=...
export GROQ_MODEL=<your-groq-model-id>
```

Other places use the placeholders `GROQ_MODEL` (sample `.jsonl` batch files, filled in
at upload time) and `YOUR_GROQ_MODEL` (curl / config snippets in READMEs).
