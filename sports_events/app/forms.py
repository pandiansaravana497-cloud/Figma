"""
forms.py
Form validation helpers.
"""

import re
from typing import Dict, Tuple


def validate_registration(data: Dict) -> Tuple[bool, Dict[str, str]]:
    """
    Validate registration form data.
    Returns (is_valid, errors_dict).
    """
    errors = {}

    name = data.get("full_name", "").strip()
    if not name:
        errors["full_name"] = "Full name is required."
    elif len(name) < 2:
        errors["full_name"] = "Name must be at least 2 characters."

    email = data.get("email", "").strip()
    pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    if not email:
        errors["email"] = "Email address is required."
    elif not re.match(pattern, email):
        errors["email"] = "Please enter a valid email address."

    event_id = data.get("event_id")
    if not event_id:
        errors["event_id"] = "Please select an event."

    return (len(errors) == 0, errors)
