from io import StringIO
import sys


class Fruit:
    def __init__(self, name, price_per_unit, days_until_expired, nr_units=1):
        self.name = name
        self.nr_units = nr_units
        self.price_per_unit = price_per_unit
        self.days_until_expired = days_until_expired


    def calculate_price(self):
        return self.nr_units * self.price_per_unit


def get_fruits():
    apples = Fruit(name='apples',
                   price_per_unit=1,
                   nr_units=10,
                   days_until_expired=25)

    bananas = Fruit(name='bananas',
                    price_per_unit=2,
                    nr_units=6,
                    days_until_expired=7)

    oranges = Fruit(name='oranges',
                    price_per_unit=3,
                    nr_units=2,
                    days_until_expired=20)

    return apples, bananas, oranges


class Basket:
    def __init__(self):
        self.content = []

    def add_item(self, item):
        self.content.append(item)

    def remove_item(self, item):
        self.content.remove(item)

    def check_for_items_close_to_expire(self, n_days):
        for item in self.content:
            if item.days_until_expired <= n_days:
                print('The item {0} will expire in {1} days'.format(
                    item.name, item.days_until_expired))

    def check_total_price(self):
        total_price = 0
        for item in self.content:
            total_price += item.calculate_price()
        print('The total price is {0}'.format(total_price))

    def examine_basket(self):
        self.check_total_price()
        for item in self.content:
            print('- {0} {1} (total price {2})'.format(
                item.nr_units, item.name, item.calculate_price()))


class Toiletpaper:
    def __init__(self, name, price_per_unit, thickness, days_until_expired, nr_units=1):
        self.name = name
        self.thickness = thickness
        self.price_per_unit = price_per_unit
        self.nr_units = nr_units
        self.days_until_expired = days_until_expired

    def calculate_price(self):
        return self.price_per_unit


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


import hashlib


def _hash(s):
    return hashlib.blake2b(bytes(s, encoding='utf8'), digest_size=5).hexdigest()


import inspect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.average_grade = None


def exercise_1_grading(pears, tangerines):
    for f in [pears, tangerines]:
        assert isinstance(f, Fruit)
    assert pears.price_per_unit == 3
    assert pears.name == 'pears'
    assert pears.nr_units == 4
    assert pears.days_until_expired == 14

    assert tangerines.price_per_unit == 6
    assert tangerines.name == 'tangerines'
    assert tangerines.nr_units == 2
    assert tangerines.days_until_expired == 2


def exercise_2_grading(calculate_price_of_all_fruits):
    apples, bananas, oranges = get_fruits()
    source = inspect.getsource(calculate_price_of_all_fruits)
    assert "return" in source, 'Did you forget to return?'
    assert ".calculate_price()" in source, 'We want you to use the .calculate_price method. Maybe you did the multiplication by hand instead?'
    assert "28" not in source, 'No answers in the function please. Sneaky sneaky.'

    assert calculate_price_of_all_fruits(
        [apples, bananas]), 'Tried running, but got nothing back. Are you returning anything?'

    error = "The total price seems wrong, maybe test it with some fruits from exercise 1?"
    assert calculate_price_of_all_fruits([apples, bananas, oranges]) == 28, error


def exercise_3_grading(my_basket, toilet_paper):
    assert isinstance(my_basket, Basket), 'Where is my_basket? Why is not a Basket?'
    assert isinstance(toilet_paper, Toiletpaper), 'Did you instanciate the toilet paper?'
    assert toilet_paper.thickness == 'Double leaf', 'How thick is this toilet paper?'

    total_value_in_basket = sum([item.calculate_price() for item in my_basket.content])
    assert total_value_in_basket <= 35, 'The basket is too expensive!'
    assert total_value_in_basket >= 30, 'The basket is not expensive enough!'

    for item in my_basket.content:
        if item.days_until_expired < 8:
            raise ValueError('There is something in your basket that will expire soon!')

    with Capturing() as output:
        my_basket.examine_basket()
    fruit_options = ['apples', 'pears', 'oranges', 'tangerines', 'bananas']
    assert sum([fruit in ''.join(output) for fruit in fruit_options]) >= 3, 'Not enough types of fruit!'
    assert Toiletpaper in [type(item) for item in my_basket.content], 'Forgot the toiletpaper? Big mistake...'


def exercise_4_grading(Student, maria, minh, sam):
    # tests for the student class
    assert Student, 'Where is the Student class?'
    assert hasattr(Student, '__init__'), 'What about the __init__?'

    # is the signature correct?
    sig = str(inspect.signature(Student.__init__))
    assert 'self' in sig, 'missing a self somewhere'
    assert ('name' in sig) and ('age' in sig), 'The __init__ signature has problems'
    assert 'average_grade' not in sig, 'Do you really need to pass an average_grade every time there is a new student?'

    # does it have the right attributes?
    source = inspect.getsource(Student.__init__).replace(" ", "")
    assert 'self.name=' in source, 'What about the name?'
    assert 'self.age=' in source, 'What about the student age?'
    assert 'self.average_grade=' in source, 'What about the average grade?'

    # did they create the right students?
    assert sum([student.age for student in [minh, maria, sam]]) == 36, 'Are their ages correct?'
    assert [minh.name, maria.name, sam.name] == ['Minh Hoang', 'Maria Dominguez',
                                                 'Sam Hopkins'], 'do they have the right names?'


def exercise_5_grading(School, test_school):
    assert isinstance(test_school.students, list), 'How will you keep track of students?'
    assert len(test_school.students) == 0, 'What are students doing in this school?'
    assert hasattr(School, '__init__'), 'Where is the __init__?'
    assert hasattr(School, 'accept_student'), 'We cannot accept students?'

    sig = inspect.signature(School.__init__)
    for key in 'self', 'name':
        assert key in sig.parameters.keys(), 'What should your accept_student method take as arguments?'

    sig = inspect.signature(School.accept_student)
    for key in 'self', 'student':
        assert key in sig.parameters.keys(), 'What should your accept_student method take as arguments?'

    tina_fey = Student(name="Tina Fey", age=16)
    test_school.accept_student(tina_fey)
    assert len(test_school.students) == 1, 'Failing to accept students, please investigate'
    assert isinstance(test_school.students[0], Student), 'Tried and failed to accept a student, please investigate'

    sig = inspect.signature(School)
    assert len(sig.parameters.keys()) == 1, 'Only expected one parameter to instanciate'
    assert list(sig.parameters.keys())[0] == 'name', 'Expected the school to have a name'


def exercise_6_grading(Highschool, happy_highschool):
    assert hasattr(Highschool, '__init__')
    assert hasattr(Highschool, 'consider_student_application')
    assert hasattr(Highschool, 'accept_student')
    assert hasattr(Highschool, 'show_all_students')

    sig = inspect.signature(Highschool)
    assert len(sig.parameters.keys()) == 1, 'Only expected one parameter to instanciate'
    assert list(sig.parameters.keys())[0] == 'name', 'Expected the Highschool to have a name'
    assert 'self' in str(inspect.signature(Highschool.__init__)), 'Check the self in your __init__'
    assert 'self' in str(inspect.signature(Highschool.accept_student)), 'Check the self in your accept_student'
    assert 'self' in str(
        inspect.signature(Highschool.consider_student_application)), 'Check the self in consider_student_application'
    assert 'self' in str(inspect.signature(Highschool.show_all_students)), 'Check the self in your show_all_students'

    assert happy_highschool.name == 'The happy highschool', 'Is the happy_highschool named correctly?'
    with Capturing() as output:
        happy_highschool.show_all_students()
    students_in_the_highschool = ''.join(output)
    assert 'Minh' in students_in_the_highschool, 'Why is Minh not in the happy highschool?'
    assert 'Maria' in students_in_the_highschool, 'Why is Maria not in the happy highschool?'
    assert 'Sam' not in students_in_the_highschool, 'How did Sam get into the happy highschool?'
    # let's make Sam try to sneak in, dispite being too young
    sam = Student(name='Sam Hopkins', age=8)
    happy_highschool.consider_student_application(sam)
    with Capturing() as output:
        happy_highschool.show_all_students()
    students_in_the_highschool = ''.join(output)
    assert 'Sam' not in students_in_the_highschool, 'Looks like Sam would be able to get into the happy highschool if he tried... Are you checking ages?'


def exercise_7_grading(Employee, Company):
    # testing creation of employees
    test_employee = Employee(name='test employee', salary=2)
    assert (test_employee.name == 'test employee') and (test_employee.salary == 2), 'problems creating employees'

    # testing creation of companies and hiring
    test_company = Company(name='test company')
    assert (test_company.name == 'test company') and (
            test_company.list_of_employees == []), 'problems creating companies'
    test_company.hire(test_employee)
    test_company.give_a_raise(test_employee, .2)
    assert test_employee.salary == 2.4, 'You may have an issue with your give_a_raise function'

    # testing methods
    test_company = Company(name='test company')
    test_employee = Employee(name='test employee', salary=2)
    test_employee_2 = Employee(name='test employee 2', salary=4)
    test_company.hire(test_employee)
    test_company.hire(test_employee_2)
    assert len(test_company.list_of_employees) == 2, 'You may have a problem with your hire method'
    test_company.give_everyone_a_raise(raise_fraction=.4)
    test_company.give_everyone_a_raise(raise_fraction=.6)
    assert hasattr(test_company, 'give_everyone_a_raise'), 'Expected method give_everyone_a_raise in Company'
    assert hasattr(test_company, 'give_a_raise'), 'Expected method give_a_raise in Company'

    big_help = """\n
    The mean salary is not correct after 2 different raises.
    
    You are close, so we'll help you out with a big clue: 
        - create a company 
        - hire two employees, one with a salary of 50, and another of 30 
        - give everyone a raise of .2, and then again of .7 
        - the mean salary should be 81.6   
    
    We hope that helps! 
    """

    assert round(test_company.get_mean_salary(), 1) == 6.7, big_help
    source = inspect.getsource(Company.give_everyone_a_raise)

    error_msg = (
        'We expect you to use the give_a_raise method inside the give_everyone_a_raise method. ' +
        '\nHint: review the last section of notebook 3.')
    assert "self.give_a_raise(" in source, error_msg


def exercise_8_grading(generous_company, stingy_company, Employee):
    assert "Generous" in generous_company.name
    assert "Burns" in stingy_company.name

    for company in [generous_company, stingy_company]:
        assert len(company.list_of_employees) == 3

    assert stingy_company.list_of_employees

    assert all([isinstance(employee, Employee)
                for employee in stingy_company.list_of_employees
                + generous_company.list_of_employees]), 'Not all employees are Employees'

    def find_carol(employees):
        for employee in employees:
            if employee.name == 'Carol M':
                return employee

    carol = find_carol(stingy_company.list_of_employees)
    assert carol, "Cannot find Carol M in the Mr. Burns Enterprises Ltd. company."

    assert round(stingy_company.get_mean_salary(), 1) == 8.9
    assert round(generous_company.get_mean_salary(), 1) == 13.3
