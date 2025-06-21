from toolbox import digit_sum, word_count, c_to_f

def test_digit_sum():
    assert digit_sum(234) == 9

def test_word_count():
    assert word_count(["hello", "world"]) == 2

def test_c_to_f():
    assert c_to_f(0) == 32
