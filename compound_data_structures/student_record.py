student_records = {
    'John': {
        'age': 20,
        'major': 'Computer Science',
        'grades': [85, 90, 92]
    },
    'Emma': {
        'age': 19,
        'major': 'Mathematics',
        'grades': [95, 88, 91]
    }
}
student_records['Alex'] = {
    'age': 21,
    'major': 'Physics',
    'grades': [80, 85, 88]
}
student_records['John']['grades'].append(88)
print(student_records)
