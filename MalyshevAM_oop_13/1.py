import datetime

# 1. Определение класса Field
class Field:
    def __init__(self, field_type, max_length=None, null=False, default=None):
        self.field_type = field_type
        self.max_length = max_length
        self.null = null
        self.default = default

    def to_sql(self):
        type_map = {
            str: 'VARCHAR',
            int: 'INTEGER',
            datetime.date: 'DATE'
        }
        sql_type = type_map.get(self.field_type, 'VARCHAR')
        constraints = []

        if self.max_length:
            constraints.append(f'({self.max_length})')
        if not self.null:
            constraints.append('NOT NULL')
        if self.default is not None:
            constraints.append(f"DEFAULT '{self.default}'")

        return f"{sql_type} {' '.join(constraints)}"

# 2. Реализация классов-типов данных
class CharField(Field):
    def __init__(self, max_length=255, null=False, default=''):
        super().__init__(str, max_length, null, default)

class IntegerField(Field):
    def __init__(self, null=False, default=0):
        super().__init__(int, null=null, default=default)

class DateField(Field):
    def __init__(self, null=False, default=datetime.date.today()):
        super().__init__(datetime.date, null=null, default=default)

# 3. Создание метакласса ModelBase
class ModelBase(type):
    def __new__(cls, name, bases, attrs):
        fields = {}
        for key, value in list(attrs.items()):
            if isinstance(value, Field):
                fields[key] = value
                del attrs[key]
        new_class = super().__new__(cls, name, bases, attrs)
        new_class._fields = fields
        return new_class

# 4. Создание базового класса Model
class Model(metaclass=ModelBase):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        values = ', '.join(f"'{getattr(self, name)}'" for name in self._fields.keys())
        columns = ', '.join(self._fields.keys())
        sql = f"INSERT INTO {self.__class__.__name__.lower()} ({columns}) VALUES ({values});"
        print(sql)

    @classmethod
    def create_table(cls, table_name):
        columns = ', '.join(f"{name} {field.to_sql()}" for name, field in cls._fields.items())
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
        print(sql)

# 5. Тестирование созданной программы
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
    year=2012,
)
book.save()
