from utils.walidator import FieldTypes


class ExamplesPatternForm:
    __auth_form = dict(
        name="Authorization",
        email=FieldTypes.EMAIL,
        password=FieldTypes.TEXT
    )
    __reg_form = dict(
        name="Registration",
        email=FieldTypes.EMAIL,
        birthday=FieldTypes.DATE,
        password=FieldTypes.TEXT,
        confirm_password=FieldTypes.TEXT
    )

    __order_form = dict(
        name="Order",
        phone=FieldTypes.PHONE,
        delivery_date=FieldTypes.DATE
    )

    __support_form = dict(
        name="Support",
        theme=FieldTypes.TEXT,
        trouble_text=FieldTypes.TEXT
    )

    @classmethod
    async def get_pattern_list(cls) -> list[dict]:
        patterns = [value
                    for key, value
                    in ExamplesPatternForm.__dict__.items()
                    if "_ExamplesPatternForm__" in key]
        return patterns
