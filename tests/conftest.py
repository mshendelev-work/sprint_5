import pytest
import random
import string


@pytest.fixture
def get_random_email():
    return f"ilon_mask_{random.randint(100, 999)}@yandex.ru"

@pytest.fixture
def get_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
