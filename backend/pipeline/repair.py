from models.repair_model import RepairResult


def repair_system(validation_result):

    repaired_components = []

    for error in validation_result.errors:

        if "table" in error.lower():
            repaired_components.append(
                "db_schema"
            )

        elif "endpoint" in error.lower():
            repaired_components.append(
                "api_schema"
            )

        elif "permission" in error.lower():
            repaired_components.append(
                "auth_schema"
            )

    repaired_components = list(
        set(repaired_components)
    )

    return RepairResult(
        repaired=True,
        repaired_components=repaired_components,
        message="Repair suggestions generated"
    )