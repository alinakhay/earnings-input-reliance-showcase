# Earnings Input Reliance

**How much does an LLM's answer change when one financial input changes?**

A controlled synthetic benchmark of price momentum, commentary tone and earnings
relative to expectations, evaluated using six pinned checkpoint conversions
across four model families. The models were evaluated as existing checkpoints;
no model was fine-tuned for this study.

This compact companion contains three recorded comparisons and a runnable example.
It illustrates how to inspect a matched input change and interpret the answer score.

## Explore

- [Interactive recorded-results explorer](https://huggingface.co/spaces/alinakhay/earnings-input-reliance-explorer)
- [Public benchmark dataset](https://huggingface.co/datasets/alinakhay/earnings-input-reliance-benchmark)

The dataset documents 2,016 prompt cases per checkpoint, 12,096 expanded
predictions and a separate 96-record pilot bridge, together with provenance and
limitations. The explorer lets readers compare recorded cases directly.

## Run the example

Python 3.10 or later; no package installation or model download is needed.

```bash
python demo.py
python demo.py --case phi-tone
```

For the selected Phi-3.5-mini tone comparison, reversing pessimistic to optimistic
commentary changes the recorded positive-answer score from **0.03% to 42.42%**,
a **+42.39 percentage-point** change. This is one illustrative case, not an
average effect or a claim about all announcements or models. The three example
pairs are selected for illustration and are not a representative sample.

`examples/recorded_cases.json` records exact source scenario IDs and the immutable
dataset revision. The small demo computes changes from the saved scores; it does
not run a model or generate new forecasts.

## Interpretation

The score compares the likelihoods of the requested positive/negative answer
prefixes, averaged across both A/B label assignments. It is not a calibrated
probability of a stock rising. Cases are synthetic, and there are no observed
market-return labels. Results depend on the tested checkpoint conversion,
prompt wording, answer encoding and context. They do not establish trading
profitability or an internal reasoning mechanism.

## Attribution and licenses

Alina Khay · Earnings Input Reliance Benchmark, version 1.0.0.
Original demo code: MIT (`LICENSE`). Recorded examples: CC BY 4.0
(`LICENSE_DATA`). Upstream models retain their separate licenses.
