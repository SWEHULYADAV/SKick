# ML and AI System Evaluation

## Purpose
Evaluate ML models, LLMs, agents, retrieval systems, and AI products without confusing benchmark scores with real-world capability.

## Evaluation contract
Define:
`task, population/input distribution, expected outputs, rubric/ground truth, model/runtime/version, prompt/system/tool configuration, sampling parameters, retrieval/data snapshot, metrics, failure taxonomy, repetitions/seeds, cost/latency budget`.

## Data integrity
Check train/test contamination, benchmark leakage, duplicated examples, label quality, class imbalance, temporal leakage, and whether evaluation examples reflect production distribution.

## Metrics
Choose metrics tied to the decision. Report uncertainty/variance and subgroup failures. Avoid collapsing safety, factuality, latency, cost, usefulness, and robustness into one opaque score.

## Agent evals
Separate:
- trigger/routing quality;
- planning/tool selection;
- tool execution correctness;
- source/citation support;
- task completion;
- side-effect safety;
- long-horizon recovery;
- cost/token/latency;
- output quality.

## Judge models
A model-as-judge is measurement instrumentation, not ground truth. Calibrate against human/reference cases, detect position/style bias where relevant, and preserve raw examples for qualitative review.

## Repetition
Stochastic systems require repeated runs. Record mean/distribution and failure modes, not a single lucky run.

## Versioning
Model aliases, provider backends, prompts, tool schemas, retrieval corpora, and system instructions can change behavior. Pin or record them when reproducibility matters.
