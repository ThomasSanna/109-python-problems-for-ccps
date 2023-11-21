def ryerson_letter_grade(pct):
    
    grades = [
        ("A+", 0.9, 1.0),
        ("A", 0.85, 0.89),
        ("A-", 0.8, 0.84),
        ("B+", 0.77, 0.79),
        ("B", 0.73, 0.76),
        ("B-", 0.7, 0.72),
        ("C+", 0.67, 0.69),
        ("C", 0.63, 0.66),
        ("C-", 0.6, 0.62),
        ("D+", 0.57, 0.59),
        ("D", 0.53, 0.56),
        ("D-", 0.5, 0.52),
        ("F", 0.0, 0.49)
    ]
    
    for grade, lower, higher in grades:
        if lower*150 <= pct and higher*150 >= pct:
            return grade

print(ryerson_letter_grade(15))
print(ryerson_letter_grade(80))
print(ryerson_letter_grade(142))