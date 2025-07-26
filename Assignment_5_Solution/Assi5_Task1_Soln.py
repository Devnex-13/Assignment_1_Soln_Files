# Create a Dictionary of Student Marks
marks = {
    'ravi':90,
    'paja':99,
    'niku':84,
    'aaru':82,
    'himya':44,
    'tushu':42,
    'dev':60
}

name = input("Enter the student\'s name:")
if(name in marks.keys()):
    print("{0}\'s marks: {1}".format(name,marks[name]))
else:
    print("Student not found.")