from password_checker import check_password_strength

def test_short_password():
    result = check_password_strength("abc")
    assert result["rating"] == "Weak"
