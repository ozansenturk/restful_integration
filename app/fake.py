from sqlalchemy.exc import IntegrityError
from faker import Faker
from app import db
# from app.models import Translation


# def translations(count=100):
#     fake = Faker()
#     i = 0
#     while i < count:
#         t1 = Translation(original_text=fake.street_name(),
#                     translation_text=fake.address(),
#                     date_text=fake.date_between(start_date='-1y', end_date='-1m'),
#                     creation_time=fake.date_between(start_date='-1y', end_date='-1m'))
#
#         db.session.add(t1)
#         try:
#             db.session.commit()
#             i += 1
#         except IntegrityError:
#             db.session.rollback()