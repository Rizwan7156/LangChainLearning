"""
Hours 19-20

Evaluation Agent

✅ Dataset Evaluation
✅ LangSmith Evaluation Pattern
"""

from tools.dataset_tool import (
    load_dataset
)

from tools.evaluation_tool import (
    evaluate_dataset
)


class EvaluationAgent:

    def run(self):

        dataset = load_dataset()

        result = evaluate_dataset(
            dataset
        )

        return result
