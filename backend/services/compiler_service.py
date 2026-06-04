import time

from pipeline.intent import extract_intent
from pipeline.design import generate_design
from pipeline.ui_generator import generate_ui_schema
from pipeline.db_generator import generate_db_schema
from pipeline.api_generator import generate_api_schema
from pipeline.auth_generator import generate_auth_schema
from pipeline.validator import validate_system
from pipeline.repair import repair_system
from pipeline.metrics import generate_metrics


def compile_application(prompt):

    start_time = time.time()

    intent = extract_intent(prompt)

    design = generate_design(intent)

    ui_schema = generate_ui_schema(design)

    db_schema = generate_db_schema(design)

    api_schema = generate_api_schema(db_schema)

    auth_schema = generate_auth_schema(
        intent,
        api_schema
    )

    validation = validate_system(
        ui_schema,
        db_schema,
        api_schema,
        auth_schema
    )

    repair = repair_system(
        validation
    )

    metrics = generate_metrics(
        time.time() - start_time,
        validation,
        repair
    )

    return {
        "intent": intent,
        "design": design,
        "ui_schema": ui_schema,
        "db_schema": db_schema,
        "api_schema": api_schema,
        "auth_schema": auth_schema,
        "validation": validation,
        "repair": repair,
        "metrics": metrics
    }