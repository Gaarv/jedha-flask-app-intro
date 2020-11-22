from models import User


def test_user_age():
    user = User(name="John", surname="Smith", address="54 rue Victor Hugo 69002 Lyon", date_of_birth="1984/11/19")
    assert user.age(at_date="2024/04/24") == 39