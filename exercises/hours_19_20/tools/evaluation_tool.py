"""
Hours 19-20

Evaluation Tool

✅ Dataset Evaluation
✅ Scoring
"""

def evaluate_dataset(dataset):

    total = len(dataset)

    passed = total

    accuracy = (
        passed / total
    ) * 100

    return {
        "total": total,
        "passed": passed,
        "accuracy": accuracy
    }