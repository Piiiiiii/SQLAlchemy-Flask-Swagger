from wtforms import StringField, IntegerField, FileField, MultipleFileField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError, NumberRange

from app.validators.base import BaseValidator


class PaginateValidator(BaseValidator):
    page = IntegerField(default=1)  # 当前页
    size = IntegerField(NumberRange(min=1, max=100), default=10)  # 每页条目个数

    def validate_page(self, value):
        self.page.data = int(value.data)

    def validate_size(self, value):
        self.size.data = int(value.data)
