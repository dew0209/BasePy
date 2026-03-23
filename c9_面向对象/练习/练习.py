from datetime import datetime


class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    count = 0
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        Student.count += 1
        self.stu_id = f'{datetime.now().year}{Student.count:03d}'
        self._source = {}

    @property
    def source(self):
        return self.source

    def add_source(self,subject,source):
        self._source[subject]=source


    def calcu_avg(self):
        if self._source:
            return sum(self._source.values())/len(self._source)
        else:
            return 0

    def __str__(self):
        avg_str = f'{self.calcu_avg():.2f}'.rstrip('0').rstrip('.')
        return f'{self.name}({self.age}-{self.gender}),成绩:{self._source},平均分:{avg_str}'


class Manager:
    def __init__(self):
        self.stu_list = []

    # 添加学生
    def add_student(self):
        name = input('姓名： ')
        age = input('年龄： ')
        gender = input('性别： ')
        stu = Student(name,age,gender)
        self.stu_list.append(stu)
        print(f'添加成功！学号是：{stu.stu_id}')

    # 删除学生
    def del_student(self):
        sid = input('学号： ')
        target = None
        for stu in self.stu_list:
            if stu.stu_id == sid:
                target = stu
                break

        if target:
            self.stu_list.remove(target)
            print(f'{target},删除成功')
        else:
            print('学号有误，删除失败')
    # 展示所有学生
    def show_all_student(self):
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        else:
            print('无学生')

    # 给指定学生设置成绩
    def set_score(self):
        sid = input('请输入学号：')
        for stu in self.stu_list:
            if stu.stu_id == sid:
                score = input('请输入成绩（学科-分数,学科-分数）')
                score_list = score.replace('，',',').split(',')
                for item in score_list:
                    subject,score = item.split('-')
                    score = float(score)
                    stu.add_source(subject,score)
                print('添加成功！')
                return
        print('学号有误')

    def run(self):
        while True:
            print('******学生管理******')
            print('1.添加学生')
            print('2.删除学生')
            print('3.查看所有学生')
            print('4.录入成绩')
            print('5.退出')
            print()
            chocie = input('请输入操作号：')
            print()
            if chocie == '1':
                self.add_student()
            elif chocie == '2':
                self.del_student()
            elif chocie == '3':
                self.show_all_student()
            elif chocie == '4':
                self.set_score()
            elif chocie == '5':
                print('再见！')
                break
            else:
                print('输入有误')

m1 = Manager()
m1.run()