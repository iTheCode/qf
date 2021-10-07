from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field


class CompanySchema(SQLAlchemyAutoSchema):
    class Meta:
        fields = ["social_name", "rut", "address"]
        load_instance = True

    id = auto_field()
    person_id = auto_field()
    social_name = auto_field()
    rut = auto_field()
    address = auto_field()
