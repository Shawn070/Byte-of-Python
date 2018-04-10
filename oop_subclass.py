class SchoolMember:
    '''代表我任何学校里的成员, 属于基类'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'\
                .format(self.name))

    def tell(self):
        '''告诉我有关我的细节'''
        print('Name:"{}" Age:"{}"'\
                .format(self.name, self.age), end=' ')
        # end = ' ' 避免在末尾打印出 \n


class Teacher(SchoolMember):
    '''代表一位老师, 属于子类'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Initialized Teacher: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:{:d}'.format(self.salary))


class Student(SchoolMember):
    '''代表一位学生, 属于子类'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Shawn', 23, 85)

print()
# 打印一行空白行

members = [t, s]
for member in members:
    member.tell()
    # 对全体师生工作
