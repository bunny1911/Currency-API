from marshmallow import Schema, fields


class RateSchema(Schema):
    """
    Simple rate schema
    """

    code = fields.Str()
    created_at = fields.Date()
    value = fields.Float()
