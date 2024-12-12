import datetime

class ModelBase(type):
    def __new__(cls, name, bases, attrs):
        fields = {}
        for key, value in list(attrs.items()):
            if isinstance(value, Field):
                fields[key] = value
                del attrs[key]
        attrs['_fields'] = fields
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def _create_table(cls, table_name):
        columns = []
        for field_name, field in cls._fields.items():
            columns.append(f"{field_name} {field.to_sql()}")
        columns_sql = ", ".join(columns)
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql});"
        print(sql)

class Field:
    def __init__(self, field_type, max_length=None, null=False, default=None):
        self.field_type = field_type
        self.max_length = max_length
        self.null = null
        self.default = default

    def to_sql(self):
        sql_type_map = {
            str: "VARCHAR",
            int: "INTEGER",
            datetime.date: "DATE"
        }
        sql_type = sql_type_map.get(self.field_type, "TEXT")
        constraints = []
        if self.max_length:
            constraints.append(f"({self.max_length})")
        if not self.null:
            constraints.append("NOT NULL")
        if self.default is not None:
            constraints.append(f"DEFAULT '{self.default}'" if isinstance(self.default, str) else f"DEFAULT {self.default}")
        return f"{sql_type}{''.join(constraints)}"


class CharField(Field):
    def __init__(self, max_length=255, null=False, default=""):
        super().__init__(str, max_length=max_length, null=null, default=default)


class IntegerField(Field):
    def __init__(self, null=False, default=0):
        super().__init__(int, null=null, default=default)


class DateField(Field):
    def __init__(self, null=False, default=None):
        if default is None:
            default = datetime.date.today()
        super().__init__(datetime.date, null=null, default=default)



class Model(metaclass=ModelBase):
    def __init__(self, **kwargs):
        for field_name in self._fields:
            setattr(self, field_name, kwargs.get(field_name))

    def save(self):
        values = []
        for field_name in self._fields:
            values.append(f"'{getattr(self, field_name)}'")
        columns = ", ".join(self._fields.keys())
        values_sql = ", ".join(values)
        sql = f"INSERT INTO {self.__class__.__name__.lower()} ({columns}) VALUES ({values_sql});"
        print(sql)

    @classmethod
    def create_table(cls, table_name):
        cls._create_table(cls, table_name)


class Book(Model):
    title = CharField(max_length=255)
    author = CharField(max_length=100)
    published_date = DateField()
    year = IntegerField()

# Создание таблицы
Book.create_table('books')

# Создание записи
book = Book(
    title='Python Cookbook',
    author='David Beazley',
    published_date=datetime.date(2013, 5, 10),
    year=2012
)
book.save()