from sqlalchemy import inspect, create_engine
from sqlalchemy.sql import text
from api import ApiClient

db_connection_string = 'postgresql://postgres:0000@localhost:5432/QA'
db = create_engine(db_connection_string)
inspector = inspect(db)

def test_db_connection():
    tables = inspector.get_table_names()
    print("Таблицы:", tables)

def test_insert():
    sql = text("insert into users(\"user_email\") values (:new_user_email)")
    rows = db.execute(sql, new_user_email = 'skypro111@mail.ru')

def test_add_new():
    body = api.get_company_list()
    len_before = len(body)

    user_email = "Sky2222@ya.ru"
    user_id = "526513"
    result = api.create_company(user_id, user_email)
    new_id = result["id"]

    body = api.get_company_list()
    len_after = len(body)

    db.delete(new_id)

    assert len_after - len_before == 1
    for company in body:
        if company["id"] == new_id:
            assert company["user_email"] == user_email
            assert company["user_id"] == user_id
            assert company["id"] == new_id

def test_update():

    user_email = "SkyPro@ya.ru"
    db.create(user_email)
    max_id = db.get_max_id()

    new_user_email = "SkyPro1111@ya.ru"
    new_user_id = "555544447"
    edited = api.edit(max_id, new_user_email, new_user_id)
    # Удаляем компанию:
    db.delete(max_id)
    assert edited["id"] == max_id
    assert edited["user_email"] == new_user_email
    assert edited["user_id"] == new_user_id
    assert edited["isActive"] == True