from marshmallow import Schema, fields


class HistorySchema(Schema):
    code = fields.Str()
    created_at = fields.Date()
    value = fields.Float()
