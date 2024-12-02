from marshmallow import ValidationError

def validar_json(request, schema):
    try:
        data = request.get_json()
        result = schema.load(data)
        return result, None
    except ValidationError as err:
        return None, err.messages