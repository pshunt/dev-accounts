import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CharacterClassValidator:
    """
    Require at least N of the following classes:
    - lowercase
    - uppercase
    - digit
    - symbol (punctuation/other)
    """
    def __init__(self, min_classes=3):
        self.min_classes = int(min_classes)

    def validate(self, password, user=None):
        classes_hit = 0
        if re.search(r"[a-z]", password):
            classes_hit += 1
        if re.search(r"[A-Z]", password):
            classes_hit += 1
        if re.search(r"\d", password):
            classes_hit += 1
        # Symbols: anything not letter or digit (space excluded)
        if re.search(r"[^\w\s]", password):
            classes_hit += 1

        if classes_hit < self.min_classes:
            raise ValidationError(
                _(f"Password must include at least {self.min_classes} of: "
                  "lowercase, uppercase, digits, and symbols."),
                code="password_not_enough_classes",
            )

    def get_help_text(self):
        return _(
            f"Include at least {self.min_classes} of the following: "
            "lowercase, uppercase, digits, and symbols."
        )


class EmailNotInPasswordValidator:
    """
    Forbid the password from containing the user's email or obvious parts of it.
    Works when email is the username.
    """
    def validate(self, password, user=None):
        if not user:
            return
        email = getattr(user, "email", None) or getattr(user, "username", "")
        if not email:
            return

        email_lower = email.lower()
        pwd_lower = password.lower()

        # Exact email
        if email_lower in pwd_lower:
            raise ValidationError(
                _("Password cannot contain your email address."),
                code="password_contains_email",
            )

        # Local part or domain labels
        local, _, domain = email_lower.partition("@")
        domain_labels = domain.split(".") if domain else []
        parts = set(filter(None, [local, *domain_labels]))

        for p in parts:
            if len(p) >= 3 and p in pwd_lower:
                raise ValidationError(
                    _("Password cannot contain parts of your email address."),
                    code="password_contains_email_parts",
                )

    def get_help_text(self):
        return _("Don’t include your email address or parts of it in the password.")
