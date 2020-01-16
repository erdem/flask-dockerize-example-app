from marshmallow import Schema, fields


class RequestEmailRetrieveSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.Email(dump_only=True)
    title = fields.Method("get_title")
    timestamp = fields.Str(attribute='created_at', dump_only=True)

    def get_title(self, obj):
        return obj.book.title


class RequestEmailCreateSchema(Schema):
    title = fields.Str(load_only=True)
    email = fields.Email(load_only=True)
