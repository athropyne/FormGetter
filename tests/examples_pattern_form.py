DATE = "date"
PHONE = "phone"
EMAIL = "email"
TEXT = "text"

class ExamplesPatternForm:
    __auth_form = dict(
        name="Authorization",
        email=EMAIL,
        password=TEXT
    )
    __reg_form = dict(
        name="Registration",
        email=EMAIL,
        birthday=DATE,
        password=TEXT,
        confirm_password=TEXT
    )

    __order_form = dict(
        name="Order",
        phone=PHONE,
        delivery_date=DATE
    )

    __support_form = dict(
        name="Support",
        theme=TEXT,
        trouble_text=TEXT
    )

    @classmethod
    async def get_pattern_list(cls) -> list[dict]:
        patterns = [value
                    for key, value
                    in ExamplesPatternForm.__dict__.items()
                    if "_ExamplesPatternForm__" in key]
        return patterns
