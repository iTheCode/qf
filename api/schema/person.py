from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from api.model.person import PersonModel


class PersonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PersonModel
        load_instance = True

    id = auto_field()
    name = auto_field()
    phone = auto_field()
