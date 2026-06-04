from models.metrics_model import Metrics


def generate_metrics(
    generation_time,
    validation_result,
    repair_result
):

    return Metrics(
        generation_time=round(
            generation_time,
            2
        ),
        validation_passed=validation_result.valid,
        repair_count=len(
            repair_result.repaired_components
        )
    )