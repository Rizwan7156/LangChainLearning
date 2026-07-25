"""
Hours 19-20

Dataset Tool

✅ Dataset Based Evaluation
"""

import json


def load_dataset():

    with open(
        "exercises/hours_19_20/datasets/evaluation_dataset.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)