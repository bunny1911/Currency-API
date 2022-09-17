from marshmallow import Schema, fields


class RateSchema(Schema):
    code = fields.Str()
    created_at = fields.Date()
    value = fields.Float()
