# TODO-1: add convert_to_letter_grade(score) function

def convert_to_letter_grade(score):
    """Converts a numerical score into a letter grade.

    Args:
        score (int, float): A student's numerical score.

    Returns:
        str: The corresponding upper-case letter grade.

    Raises:
        ValueError: If the score is not between 0 and 100.
        TypeError: If the score is not a numeric value.

    Letter grades are assigned as follows:
        A: 90 to 100
        B: 80 to 89
        C: 70 to 79
        D: 60 to 69
        F: Below 60
    """
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric value.")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'