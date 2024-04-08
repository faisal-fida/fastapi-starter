from typing import Any


def to_dict(model_instance) -> dict[str, Any]:
    """
    Returns a dictionary representation of a model instance.

    Includes all attributes defined on the model class.

    Args:
        model_instance: The model instance to convert to a dictionary.

    Returns:
        A dictionary containing all attributes and their values.
    """
    return {c.name: getattr(model_instance, c.name) for c in model_instance.__table__.columns}
