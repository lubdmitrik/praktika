class Srudent_grades:
    name = ""
    num_of_lectiones = 0
    max_grade = 0
    num_of_praktic_sesons = 0

    lections_visited = []
    grades_praktic = []
    def __init__(self):
        self.name = input("Введіть ім'я студента: ")
        self.num_of_lectiones = int(input("Введіть кількість лекцій: "))
        self.max_grade = int(input("Максимальний бал:"))
        self.num_of_praktic_sesons = int(input("Введіть число лабораторних занять: "))
        for i in range(0,self.num_of_praktic_sesons):
            self.grades_praktic.append(0)
        for i in range(0,self.num_of_lectiones):
               self.lections_visited.append(False)
                
    def grades_p_init (self,grade,num_of_praktic_s):
        if num_of_praktic_s > 0 and num_of_praktic_s <= self.num_of_praktic_sesons and grade > -1 and grade <= self.max_grade:
            self.grades_praktic[num_of_praktic_s-1] = grade

    def lection_init (self,lection_num_visited):
        if lection_num_visited > 0 and lection_num_visited <= self.num_of_lectiones:
            self.lections_visited[lection_num_visited-1] = True

    def grade_return (self):
        num = 0
        sum_ = 0
        for grade in self.grades_praktic:
            sum_ += grade
            num += 1
        return sum_ / num

s1 = Srudent_grades()
s1.grades_p_init(5,2)
s1.lection_init(2)
print(s1.grade_return())
