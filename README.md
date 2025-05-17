# cdxgent

This repository contains a simple HTML sketch and a Python utility for evaluating the novelty of text snippets.

## `novelty_evaluator.py`

```
usage: novelty_evaluator.py text reference [reference ...]
```

The script computes a basic novelty score for `text` against one or more reference documents using Jaccard similarity of unique words. The novelty score is `1 - max(similarity)` where `similarity` is the highest Jaccard similarity between the input and any reference.

Example:

```
python3 novelty_evaluator.py my_prompt.txt existing_prompt.txt
```

The higher the novelty score, the less overlap there is with the reference documents.
