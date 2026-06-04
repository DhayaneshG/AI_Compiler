import json
import os


def export_json(filename, data):

    os.makedirs("../outputs", exist_ok=True)

    filepath = os.path.join(
        "../outputs",
        filename
    )

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

    return filepath