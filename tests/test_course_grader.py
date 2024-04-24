import pytest
from sample.course_grader import convert_to_letter_grade

# TODO-1: Add test_exact_grade_boundaries() function

def test_exact_boundaries():
    assert convert_to_letter_grade(0) == 'F', "Score of 0 should be F"
    assert convert_to_letter_grade(59) == 'F', "Score of 59 should be F"
    assert convert_to_letter_grade(60) == 'D', "Score of 60 should be D"
    assert convert_to_letter_grade(69) == 'D', "Score of 69 should be D"
    assert convert_to_letter_grade(70) == 'C', "Score of 70 should be C"
    assert convert_to_letter_grade(79) == 'C', "Score of 79 should be C"
    assert convert_to_letter_grade(80) == 'B', "Score of 80 should be B"
    assert convert_to_letter_grade(89) == 'B', "Score of 89 should be B"
    assert convert_to_letter_grade(90) == 'A', "Score of 90 should be A"
    assert convert_to_letter_grade(100) == 'A', "Score of 100 should be A"

# TODO-2: Add test_invalid_numerical_score() function

def test_invalid_numerical_score():
    with pytest.raises(ValueError) as e_info:
        convert_to_letter_grade(-1)
    assert str(e_info.value) == "Score must be between 0 and 100.", "Negative scores should raise ValueError with proper message"
    
    with pytest.raises(ValueError) as e_info:
        convert_to_letter_grade(101)
    assert str(e_info.value) == "Score must be between 0 and 100.", "Scores above 100 should raise ValueError with proper message"

# TODO-3: Add test_non_numeric_input() function

def test_non_numeric_type():
    with pytest.raises(TypeError) as e_info:
        convert_to_letter_grade("ninety")
    assert str(e_info.value) == "Score must be a numeric value.", "String input should raise TypeError with proper message"
    
    with pytest.raises(TypeError) as e_info:
        convert_to_letter_grade([90])
    assert str(e_info.value) == "Score must be a numeric value.", "List input should raise TypeError with proper message"
    
    with pytest.raises(TypeError) as e_info:
        convert_to_letter_grade(None)
    assert str(e_info.value) == "Score must be a numeric value.", "None input should raise TypeError with proper message"
