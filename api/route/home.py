from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from

from api.model.person import PersonModel
from api.schema.person import PersonSchema

home_api = Blueprint('api', __name__)


@home_api.route('/persona')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'API Schema',
            'schema': PersonModel
        }
    }
})
def Person():
    result = PersonModel()
    return PersonSchema().dump(result), 200
