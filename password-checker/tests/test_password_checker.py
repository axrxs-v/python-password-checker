from password_checker import check_password_strength

def test_short_password():
    result = check_password_strength("abc")
    assert result["rating"] == "Weak"

def test_strong_password():
    result = check_password_strength("Abcdef123!@#")
    assert result["rating"] == "Strong"

def test_password_without_digits():
    result = check_password_strength("Abcdef!@#")
    assert result["has_digit"] is False

def test_repeated_characters():
    result = check_password_strength("aaaBBB123!")
    assert result["no_repeats"] is False

def test_sequence_in_password():
    result = check_password_strength("Abc123!@#")
    assert result["no_sequences"] is False
