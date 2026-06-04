from models.validation_model import ValidationResult


def validate_system(
    ui_schema,
    db_schema,
    api_schema,
    auth_schema
):

    errors = set()

    # DB table names
    table_names = [
        table.name.lower()
        for table in db_schema.tables
    ]

    # API endpoint validation
    for endpoint in api_schema.endpoints:

        endpoint_name = (
            endpoint.path
            .split("/")[1]
            .lower()
        )

        if endpoint_name not in table_names:
            errors.add(
                f"Missing table for endpoint: {endpoint.path}"
            )

    valid = len(errors) == 0

    return ValidationResult(
    valid=valid,
    errors=list(errors)
)