class Student:
    print('Welcome To Sinhgad Academy Of Engineering, Pune.')

    def __init__(self, name, marks):
        self.name= name
        self.marks= marks
    def welcome(self):
        print(f'Welcome {self.name} in Sinhgad Academy Of Engineering, Pune.')
    def get_avg(self):
        marks= self.marks
        sum=0
        for val in marks:
            sum+=val
        return sum/len(self.marks)

lst= list()
print('Enter the marks of Best Of 5 Subject:\n')
for i in range(1, 6):
    lst.append(int(input(f'Enter mark of subject {i}:')))

name= input('Enter Your Full Name:')

# Object creation
s1= Student(name, lst)
s1.welcome()
print(f'{s1.name} Your Average marks is:',s1.get_avg())