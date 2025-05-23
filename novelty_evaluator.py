import argparse
import re
from typing import List, Tuple

# Function to tokenize text into lowercase words without punctuation
TOKEN_RE = re.compile(r"[A-Za-z0-9']+")

def tokenize(text: str) -> List[str]:
    return TOKEN_RE.findall(text.lower())

# Function to compute Jaccard similarity between two token sets

def jaccard_similarity(a: List[str], b: List[str]) -> float:
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 1.0
    return len(sa & sb) / len(sa | sb)


def evaluate_novelty(text: str, references: List[str]) -> Tuple[float, float]:
    """Return novelty score (1 - max Jaccard) and best similarity."""
    tokens = tokenize(text)
    if not tokens:
        return 0.0, 0.0
    similarities = []
    for ref in references:
        similarities.append(jaccard_similarity(tokens, tokenize(ref)))
    best_sim = max(similarities) if similarities else 0.0
    return 1.0 - best_sim, best_sim


def main():
    parser = argparse.ArgumentParser(description="Evaluate text novelty")
    parser.add_argument("text", help="Path to the text file to evaluate")
    parser.add_argument("references", nargs="*", help="Paths to reference text files")
    args = parser.parse_args()

    with open(args.text, "r", encoding="utf-8") as f:
        text = f.read()

    references = []
    for path in args.references:
        with open(path, "r", encoding="utf-8") as f:
            references.append(f.read())

    novelty, similarity = evaluate_novelty(text, references)
    print(f"Novelty score: {novelty:.3f}")
    print(f"Best similarity to reference: {similarity:.3f}")

if __name__ == "__main__":
    main()
