import pytest


from app.main import check_password


def test_valid_password():
    assert check_password("Passw@rd1") is True


def test_small_password():
    assert check_password("p@E3") is False


def test_lower_password():
    assert check_password("qwerty") is False


def test_minimum_length_valid():
    assert check_password("Pas$w0rd") is True


def test_too_long_password():
    assert check_password("Password@23123421") is False


def test_no_digits():
    assert check_password("Pass@word") is False


def test_no_specials():
    assert check_password("Password321") is False


def test_no_upper_letter():
    assert check_password("pass@word123") is False


def test_space_in_password():
    assert check_password("Password@ 321") is False


def test_all_special_characters():
    assert check_password("$@#&!-_") is False


def test_only_digits():
    assert check_password("12345678") is False


def test_only_letters():
    assert check_password("Password") is False


def test_empty_string():
    assert check_password("") is False


def test_exactly_7_chars():
    assert check_password("Pa@s1wo") is False