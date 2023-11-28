# sort() method     = used with lists
# sort() functin    = used with iterables

students = [('João', 'A', 22),
            ('Rhuan', 'B', 23),
            ('Julio', 'A', 24),
            ('Garcia', 'E', 33),
            ('Gabriel', 'C', 28)]

nome = lambda nomes: nomes[0]

sorted_students = students.sort(key=nome)

for i in students:
    print(i)