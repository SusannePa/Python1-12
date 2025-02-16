# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.
"""
phone_numbers = { 'Jack': '070-02222748',
                      'Pete': '010-2488634' }
my_empty_dict = { }
phone_numbers['Jack']
'070-02222748'
"""

def create_student_register(students: list) -> dict:
    """
    Tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet
    """
    student_register = {}
    for name, age in students:
        student_register[name] = age
    return student_register
"""
def test_create_student_register():
    students = [("Anna", 20), ("Bertil", 25), ("Cecilia", 22)]
    assert create_student_register(students) == {"Anna": 20, "Bertil": 25, "Cecilia": 22}
"""
students = [("Arne", 20), ("Berit", 25), ("Carl", 22)]
studDict = create_student_register(students)
print(studDict.get('Carl'))

