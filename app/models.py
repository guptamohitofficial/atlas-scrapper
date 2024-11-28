from peewee import Model, SqliteDatabase, PostgresqlDatabase, CharField, FloatField, IntegerField
import config as settings

if settings.DB_TYPE == 'sqlite':
    db = SqliteDatabase(settings.DB_NAME)
elif settings.DB_TYPE == 'postgresql':
    db = PostgresqlDatabase(
        settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST
    )
else:
    raise TypeError("Unsupported DB_TYPE")

class BaseModel(Model):
    class Meta:
        database = db

class Product(BaseModel):
    title = CharField()
    price = FloatField()
    image_url = CharField()

db.connect()
db.create_tables([Product], safe=True)
