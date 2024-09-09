from django.core.management import BaseCommand

from catalog.models import Student


class Command(BaseCommand):


    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'Petrov', 'first_name': 'Petr'},
            {'last_name': 'Ivanov', 'first_name': 'Ivan'},
            {'last_name': 'Sidorov', 'first_name': 'Sidor'},
            {'last_name': 'Vasechkin', 'first_name': 'Vasech'}
        ]


        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        students_for_create = []
        for student_item in student_list:
            students_for_create.append(Student(**student_item))

        Student.objects.bulk_create(students_for_create)


