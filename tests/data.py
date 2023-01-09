


class FakeData:
    EMAIL__ = "example.001@gmail.com"  # valid email
    V1_DATE__ = "06.10.1990"  # valid date format v1
    V2_DATE__ = "1990-10-06"  # valid date format v2
    PHONE__ = "+7 903 016 06 15"  # valid phone
    TEXT__ = "lorem ipsum"  # text or no valid field

    valid_registration_form = dict(
        email=EMAIL__,
        birthday=V1_DATE__,
        password=TEXT__,
        confirm_password=TEXT__
    )
    valid_authorization_form = dict(
        email=EMAIL__,
        password=TEXT__
    )
    valid_order_form = dict(
        phone=PHONE__,
        delivery_date=V2_DATE__
    )
    valid_support_form = dict(
        theme=TEXT__,
        trouble_text=TEXT__
    )
    similar_registration_form = dict(
        email=EMAIL__,
        birthday=V1_DATE__,
        password=TEXT__,
        confirm_password=TEXT__,
        phone=PHONE__,
        fake_field1=EMAIL__,
        fake_field2=TEXT__
    )
    similar_authorization_form = dict(
        email=EMAIL__,
        password=TEXT__,
        birthday=V1_DATE__,
    )
    similar_order_form = dict(
        phone=PHONE__,
        delivery_date=V2_DATE__,
    )
    similar_support_form = dict(
        theme=TEXT__,
        trouble_text=TEXT__,
        fale_field=EMAIL__,
    )
    similar_authorization_and_support_form = dict(
        theme=TEXT__,
        trouble_text=TEXT__,
        email=EMAIL__,
        password=TEXT__
    )  # return two form name (config.ONE_PATTERN_ONLY = True) or generated pattern (config.ONE_PATTERN_ONLY = False)
    no_valid_form = dict(
        fake_field1=EMAIL__,
        fake_field2=TEXT__,
        fake_field3=PHONE__
    )  # return generated pattern
    similar_multy = dict(
        email=EMAIL__,
        birthday=V1_DATE__,
        password=TEXT__,
        confirm_password=TEXT__,
        phone=PHONE__,
        delivery_date=V2_DATE__,
        theme=TEXT__,
        trouble_text=TEXT__
    )

    @staticmethod
    def get_all_fake_data__() -> list[dict]:
        test_requests = [i for i in FakeData.__dict__ if not i.endswith("__")]
        data = [FakeData.__dict__[i] for i in test_requests]
        return data
